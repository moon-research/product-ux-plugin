#!/usr/bin/env python3
"""Create a non-overwriting skills-only release ZIP from validated inputs."""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import zipfile


spec = importlib.util.spec_from_file_location("product_ux_validate", Path(__file__).with_name("validate.py"))
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def create_archive(root: Path, output: Path) -> list[str]:
    root = root.resolve()
    errors = validator.validate(root)
    if errors:
        raise ValueError("Package validation failed:\n" + "\n".join(errors))
    paths = validator.distribution_files(root)
    if output.resolve() in {path.resolve() for path in paths}:
        raise ValueError("Archive output must not replace a distributed file")
    names = []
    # x creates exclusively, including when an existing path is a symlink.
    with output.open("xb") as file:
        try:
            with zipfile.ZipFile(file, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                for path in paths:
                    name = path.relative_to(root).as_posix()
                    info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, path.read_bytes())
                    names.append(name)
        except BaseException:
            output.unlink(missing_ok=True)
            raise
    return names


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        names = create_archive(args.root, args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"ERROR: {error}\n")
    print(f"Created {args.output}: {len(names)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
