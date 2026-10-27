#!/usr/bin/env python3
"""Validate this skills-only distribution without installing dependencies."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


MANIFESTS = ("plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json")
CATALOGS = (".claude-plugin/marketplace.json", ".agents/plugins/marketplace.json")
DOCUMENTS = ("README.md", "LICENSE", "NOTICE")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def distribution_files(root: Path) -> list[Path]:
    """Explicit publish boundary; repository setup, tests and notes never ship."""
    paths = [root / name for name in (*MANIFESTS, *CATALOGS, *DOCUMENTS)]
    skills = root / "skills"
    if skills.is_symlink():
        raise ValueError(f"symlink is not distributable: {skills}")
    if skills.is_dir():
        for path in sorted(skills.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"symlink is not distributable: {path}")
            if path.is_file():
                parts = path.relative_to(skills).parts
                if any(part in {".git", "__pycache__", ".DS_Store", "node_modules", ".wrangler", ".superdesign"}
                       or part == ".env" or part.startswith(".env.") for part in parts) or path.suffix in {".pyc", ".pyo"}:
                    raise ValueError(f"local artifact is not distributable: {path}")
                paths.append(path)
    for path in paths:
        if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != root.parent):
            raise ValueError(f"symlink is not distributable: {path}")
    return sorted(paths)


def read_json(root: Path, name: str, errors: list[str]) -> dict:
    try:
        data = json.loads((root / name).read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("expected a JSON object")
        return data
    except (OSError, ValueError) as error:
        errors.append(f"{name}: {error}")
        return {}


def frontmatter(text: str) -> dict[str, str]:
    """Read the deliberately small scalar subset used by this package."""
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("expected YAML frontmatter")
    header = text[4:].split("\n---\n", 1)[0]
    fields = {}
    for line in header.splitlines():
        key, separator, value = line.partition(":")
        if not separator or key not in ("name", "description") or key in fields:
            raise ValueError(f"unexpected or duplicate frontmatter field: {key}")
        value = value.strip()
        fields[key] = json.loads(value) if value.startswith('"') else value
    return fields


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    manifests = [read_json(root, name, errors) for name in MANIFESTS]
    identity = manifests[0]
    for name, manifest in zip(MANIFESTS, manifests):
        for key in ("name", "version", "description"):
            if not isinstance(manifest.get(key), str) or not manifest[key].strip():
                errors.append(f"{name}: missing {key}")
            elif manifest[key] != identity.get(key):
                errors.append(f"{name}: {key} differs from plugin.json")
    if not NAME.fullmatch(str(identity.get("name", ""))):
        errors.append("plugin.json: invalid name")
    if identity.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json: missing portable Agent Plugins schema")
    if manifests[2].get("skills") != "./skills/":
        errors.append(".codex-plugin/plugin.json: skills must be ./skills/")

    catalogs = [read_json(root, name, errors) for name in CATALOGS]
    for name, catalog in zip(CATALOGS, catalogs):
        if not catalog.get("name") or catalog.get("name") != catalogs[0].get("name"):
            errors.append(f"{name}: marketplace name is missing or differs")
        entries = catalog.get("plugins")
        if not isinstance(entries, list) or len(entries) != 1 or not isinstance(entries[0], dict):
            errors.append(f"{name}: expected one plugin entry")
            continue
        entry = entries[0]
        if entry.get("name") != identity.get("name"):
            errors.append(f"{name}: plugin identity differs")
        source = entry.get("source")
        if source != "./" and source != {"source": "local", "path": "./"}:
            errors.append(f"{name}: source must point at this package root (./)")

    try:
        paths = distribution_files(root)
    except ValueError as error:
        return errors + [str(error)]
    available = {path.resolve() for path in paths}
    for path in paths:
        if not path.is_file():
            errors.append(f"missing distribution file: {path.relative_to(root)}")
    skill_files = sorted((root / "skills").glob("*/SKILL.md"))
    if not skill_files:
        errors.append("skills/: no discoverable skills")
    for path in skill_files:
        try:
            fields = frontmatter(path.read_text(encoding="utf-8"))
            if fields.get("name") != path.parent.name or not NAME.fullmatch(fields.get("name", "")):
                errors.append(f"{path.relative_to(root)}: name must match the skill folder")
            description = fields.get("description", "")
            if not isinstance(description, str) or not description.strip() or len(description) > 1024:
                errors.append(f"{path.relative_to(root)}: invalid description")
        except (OSError, ValueError) as error:
            errors.append(f"{path.relative_to(root)}: {error}")

    for path in paths:
        if path.suffix != ".md" or not path.is_file():
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            url = urlsplit(link)
            if url.scheme in ("https", "http", "mailto"):
                continue
            if url.scheme or url.netloc or Path(url.path).is_absolute():
                errors.append(f"{path.relative_to(root)}: outside package link {link}")
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if not target.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: outside package link {link}")
            elif target not in available or not target.is_file():
                errors.append(f"{path.relative_to(root)}: reference is not distributed: {link}")
            elif url.fragment and target.suffix == ".md":
                headings = re.findall(r"^#{1,6}\s+(.+)", target.read_text(encoding="utf-8"), re.M)
                anchors = {re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings}
                if unquote(url.fragment) not in anchors:
                    errors.append(f"{path.relative_to(root)}: missing heading: {link}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    count = len(list((args.path / "skills").glob("*/SKILL.md")))
    print(f"Valid package: {count} shared skills, matching manifests/catalogs, contained references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
