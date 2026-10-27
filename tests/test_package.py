"""Exercise package boundaries in disposable directories, not this working tree."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
import zipfile


REPO = Path(__file__).resolve().parents[1]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validator = load("validate")
packager = load("package")


def write(root: Path, path: str, content: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def write_json(root: Path, path: str, data: dict) -> None:
    write(root, path, json.dumps(data))


def fixture(root: Path) -> None:
    identity = {"name": "example-ux", "version": "0.1.0", "description": "Example UX skills"}
    write_json(root, "plugin.json", {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", **identity,
    })
    write_json(root, ".claude-plugin/plugin.json", identity)
    write_json(root, ".codex-plugin/plugin.json", {**identity, "skills": "./skills/"})
    entry = {"name": identity["name"], "source": "./"}
    write_json(root, ".claude-plugin/marketplace.json", {
        "name": "example-market", "owner": {"name": "Example"}, "plugins": [entry],
    })
    write_json(root, ".agents/plugins/marketplace.json", {
        "name": "example-market", "plugins": [{**entry,
            "policy": {"installation": "AVAILABLE", "authentication": "ON_USE"},
            "category": "Productivity"}],
    })
    write(root, "skills/example/SKILL.md", '---\nname: example\ndescription: "Use when reviewing a product brief."\n---\n\nRead [the guide](references/guide.md).\n')
    write(root, "skills/example/references/guide.md", "# Guide\n\nUse the supplied evidence.\n")
    write(root, "skills/example/agents/openai.yaml", 'interface:\n  display_name: "Example UX"\n  short_description: "Review a product brief and its evidence"\n  default_prompt: "Use $example to review this brief."\n')
    for path in ("README.md", "LICENSE", "NOTICE"):
        write(root, path, "Example distribution document.\n")


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="product-ux-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "plugin"
        self.root.mkdir()
        fixture(self.root)

    def test_valid_package_can_move_to_another_directory(self):
        self.assertEqual([], validator.validate(self.root))

    def test_rejects_manifest_identity_drift(self):
        path = self.root / ".codex-plugin/plugin.json"
        data = json.loads(path.read_text())
        data["version"] = "9.9.9"
        path.write_text(json.dumps(data))
        self.assertTrue(any("version" in e for e in validator.validate(self.root)))

    def test_rejects_missing_reference(self):
        (self.root / "skills/example/references/guide.md").unlink()
        self.assertTrue(any("guide.md" in e for e in validator.validate(self.root)))

    def test_rejects_reference_outside_distribution(self):
        write(self.root, "skills/example/SKILL.md", '---\nname: example\ndescription: "Use when reviewing a brief."\n---\n[private](../../../private.md)\n')
        self.assertTrue(any("outside" in e for e in validator.validate(self.root)))

    def test_rejects_symlink_in_distributable_tree(self):
        (self.root / "skills/example/references/linked.md").symlink_to(self.root / "README.md")
        self.assertTrue(any("symlink" in e.lower() for e in validator.validate(self.root)))

    def test_rejects_local_artifacts_nested_inside_skills(self):
        for path in (".env", ".env.local", ".git/config", "__pycache__/local.pyc", ".DS_Store"):
            with self.subTest(path=path):
                nested = "skills/example/" + path
                write(self.root, nested, "private local data")
                errors = validator.validate(self.root)
                self.assertTrue(any("local artifact" in e for e in errors), errors)
                target = Path(self.temp.name) / "unsafe.zip"
                with self.assertRaises(ValueError):
                    packager.create_archive(self.root, target)
                self.assertFalse(target.exists())
                (self.root / nested).unlink()

    def test_rejects_skill_name_mismatch(self):
        path = self.root / "skills/example/SKILL.md"
        path.write_text(path.read_text().replace("name: example", "name: different"))
        self.assertTrue(any("name" in e for e in validator.validate(self.root)))

    def test_rejects_empty_skills_tree(self):
        import shutil
        shutil.rmtree(self.root / "skills")
        self.assertTrue(any("skill" in e.lower() for e in validator.validate(self.root)))

    def test_rejects_escaping_marketplace_source(self):
        path = self.root / ".agents/plugins/marketplace.json"
        data = json.loads(path.read_text())
        data["plugins"][0]["source"] = {"source": "local", "path": "../other"}
        path.write_text(json.dumps(data))
        self.assertTrue(any("source" in e for e in validator.validate(self.root)))

    def test_archive_excludes_repository_setup_and_private_files(self):
        for path in (".env", "setup-ux.sh", "docs/private.md", ".git/config", "tests/secret.json"):
            write(self.root, path, "must not ship")
        target = Path(self.temp.name) / "release.zip"
        packager.create_archive(self.root, target)
        with zipfile.ZipFile(target) as archive:
            names = archive.namelist()
            self.assertIn("plugin.json", names)
            self.assertIn(".claude-plugin/plugin.json", names)
            self.assertIn(".codex-plugin/plugin.json", names)
            self.assertIn("skills/example/SKILL.md", names)
            self.assertTrue(all(not n.startswith(("/", "../")) for n in names))
            for forbidden in (".env", "setup-ux.sh", "docs/private.md", ".git/config", "tests/secret.json"):
                self.assertNotIn(forbidden, names)
            destination = Path(self.temp.name) / "extracted"
            archive.extractall(destination)
        self.assertEqual([], validator.validate(destination))

    def test_archive_never_overwrites_existing_output(self):
        target = Path(self.temp.name) / "release.zip"
        target.write_bytes(b"retain me")
        with self.assertRaises(FileExistsError):
            packager.create_archive(self.root, target)
        self.assertEqual(b"retain me", target.read_bytes())

    def test_invalid_package_is_not_archived(self):
        (self.root / ".claude-plugin/plugin.json").unlink()
        target = Path(self.temp.name) / "invalid.zip"
        with self.assertRaises(ValueError):
            packager.create_archive(self.root, target)
        self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
