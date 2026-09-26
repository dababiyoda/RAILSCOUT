"""CLI: python -m railscout appraise INPUT.json --source-root DIR --output RECEIPT.json"""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile

from .appraise import AppraisalError, appraise, verify


def _write_new(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise AppraisalError(f"refusing to overwrite receipt: {path}")
    payload = (json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n").encode()
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".railscout-", delete=False) as fh:
        temporary = Path(fh.name)
        try:
            fh.write(payload)
            fh.flush()
            os.fsync(fh.fileno())
        except BaseException:
            temporary.unlink(missing_ok=True)
            raise
    try:
        os.link(temporary, path)  # exclusive: concurrent runs cannot replace a receipt
        descriptor = os.open(path.parent, os.O_RDONLY | getattr(os, "O_DIRECTORY", 0))
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
    except FileExistsError as exc:
        raise AppraisalError(f"refusing to overwrite receipt: {path}") from exc
    finally:
        temporary.unlink(missing_ok=True)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Source-bound, read-only opportunity appraisal")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("appraise", "verify"):
        command = sub.add_parser(name)
        command.add_argument("input", type=Path)
        command.add_argument("--source-root", required=True, type=Path)
        if name == "appraise":
            command.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        if args.input.stat().st_size > 1024 * 1024:
            raise AppraisalError("input exceeds 1 MiB")
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if args.command == "appraise":
            result = appraise(data, args.source_root)
            _write_new(args.output, result)
            print(json.dumps({"status": result["appraisal"]["status"],
                              "next_action": result["appraisal"]["next_action"],
                              "receipt": str(args.output), "sha256": result["receipt_sha256"]}))
        else:
            print(json.dumps(verify(data, args.source_root)))
        return 0
    except (AppraisalError, OSError, ValueError) as exc:
        print(f"RailScout refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
