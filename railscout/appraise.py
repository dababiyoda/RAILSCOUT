"""Deterministic evidence binding and abstention for a proposed opportunity.

This library evaluates *provided* sources and claims. It never treats the user's
classification of a passage as independently verified truth, and it has no
network, model, credential, market-contact or consequence authority.
"""

from __future__ import annotations

from datetime import datetime
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

VERSION = "railscout.appraisal/1"
MAX_SOURCE_BYTES = 256 * 1024
MAX_SOURCES = 12
MAX_CLAIMS = 100
LAYERS = {"proof", "trust", "eligibility", "routing", "settlement", "coordination"}
LENSES = ("commercial", "strategic", "regenerative", "institutional", "capital")


class AppraisalError(ValueError):
    """Malformed input, changed source, or unverifiable receipt."""


def _object(value: Any, label: str) -> dict:
    if not isinstance(value, dict):
        raise AppraisalError(f"{label} must be an object")
    return value


def _string(value: Any, label: str, *, required: bool = True) -> str:
    if not isinstance(value, str) or (required and not value.strip()) or len(value) > 4096:
        raise AppraisalError(f"{label} must be a bounded string")
    return value.strip()


def _canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _read_source(root: Path, source: dict) -> bytes:
    name = _string(source.get("path"), "source.path")
    relative = Path(name)
    if relative.is_absolute() or not relative.parts or ".." in relative.parts:
        raise AppraisalError(f"source path must be relative and bounded: {name}")
    candidate = root / relative
    # Symlinks anywhere in the path are refused, including a symlink to an
    # in-root file: a later retarget would invalidate a retained receipt.
    if any(part.is_symlink() for part in (candidate, *candidate.parents) if part != root):
        raise AppraisalError(f"symlink source refused: {name}")
    path = candidate.resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise AppraisalError(f"source unavailable outside root: {name}")
    with path.open("rb") as handle:
        raw = handle.read(MAX_SOURCE_BYTES + 1)
    if len(raw) > MAX_SOURCE_BYTES:
        raise AppraisalError(f"source exceeds {MAX_SOURCE_BYTES} bytes: {name}")
    try:
        raw.decode("utf-8")
    except UnicodeError as exc:
        raise AppraisalError(f"source must be UTF-8: {name}") from exc
    expected = _string(source.get("sha256"), "source.sha256")
    if len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected):
        raise AppraisalError("source.sha256 must be lowercase SHA-256 hex")
    if sha256(raw).hexdigest() != expected:
        raise AppraisalError(f"source changed: {name}")
    return raw


def appraise(manifest: dict, source_root: str | Path) -> dict:
    """Return a reproducible receipt or fail closed on missing/changed evidence."""
    manifest = _object(manifest, "manifest")
    root = Path(source_root).expanduser().resolve(strict=True)
    if not root.is_dir():
        raise AppraisalError("source root must be a directory")
    question = _string(manifest.get("question"), "question")
    transaction = _string(manifest.get("transaction"), "transaction")
    sources = manifest.get("sources")
    claims = manifest.get("claims")
    if not isinstance(sources, list) or not 1 <= len(sources) <= MAX_SOURCES:
        raise AppraisalError("sources must contain 1 to 12 entries")
    if not isinstance(claims, list) or not 1 <= len(claims) <= MAX_CLAIMS:
        raise AppraisalError("claims must contain 1 to 100 entries")

    blobs: dict[str, bytes] = {}
    source_rows = []
    for item in sources:
        source = _object(item, "source")
        sid = _string(source.get("id"), "source.id")
        if sid in blobs:
            raise AppraisalError(f"duplicate source ID: {sid}")
        _string(source.get("origin"), "source.origin")
        collected = _string(source.get("collected_at"), "source.collected_at")
        try:
            stamp = datetime.fromisoformat(collected.replace("Z", "+00:00"))
            if stamp.tzinfo is None:
                raise ValueError("timezone absent")
        except ValueError as exc:
            raise AppraisalError("source.collected_at requires a timezone-aware ISO timestamp") from exc
        _string(source.get("rights"), "source.rights")
        blob = _read_source(root, source)
        blobs[sid] = blob
        source_rows.append({"id": sid, "path": source["path"], "origin": source["origin"],
                            "sha256": source["sha256"], "bytes": len(blob),
                            "collected_at": source["collected_at"],
                            "rights": source["rights"], "rights_status": "source-declared"})

    claim_rows, seen_ids, positions = [], set(), {}
    for item in claims:
        claim = _object(item, "claim")
        cid = _string(claim.get("id"), "claim.id")
        sid = _string(claim.get("source_id"), "claim.source_id")
        topic = _string(claim.get("topic"), "claim.topic")
        assertion = _string(claim.get("assertion"), "claim.assertion")
        excerpt = _string(claim.get("excerpt"), "claim.excerpt")
        stance = claim.get("stance")
        kind = claim.get("kind")
        if cid in seen_ids or sid not in blobs:
            raise AppraisalError(f"duplicate claim or unknown source: {cid}/{sid}")
        if stance not in ("supports", "challenges") or kind not in ("observation", "allegation", "inference"):
            raise AppraisalError(f"claim {cid}: invalid stance or kind")
        seen_ids.add(cid)
        needle = excerpt.encode("utf-8")
        blob = blobs[sid]
        start = blob.find(needle)
        if start < 0 or blob.find(needle, start + 1) >= 0:
            raise AppraisalError(f"claim {cid}: excerpt missing or ambiguous in source bytes")
        positions.setdefault(topic, set()).add(stance)
        claim_rows.append({"id": cid, "source_id": sid, "topic": topic, "assertion": assertion,
                           "kind": kind, "stance": stance, "excerpt": excerpt,
                           "byte_start": start, "byte_end": start + len(needle),
                           "epistemic_status": "source-passage-verified; assertion-unverified"})

    market = _object(manifest.get("market", {}), "market")
    market_evidence = _object(market.get("evidence", {}), "market.evidence")
    failure = _object(manifest.get("failure", {}), "failure")
    layer = failure.get("layer")
    if layer not in LAYERS:
        raise AppraisalError("failure.layer must name one governing transaction layer")
    refs = failure.get("claim_ids", [])
    if not isinstance(refs, list) or not refs or any(ref not in seen_ids for ref in refs):
        raise AppraisalError("failure.claim_ids must reference source-bound claims")
    description = _string(failure.get("description"), "failure.description")
    for key in ("buyer", "budget_owner", "verifier", "accepted_decision"):
        if key in market:
            _string(market[key], f"market.{key}", required=False)
        references = market_evidence.get(key, [])
        if not isinstance(references, list) or any(ref not in seen_ids for ref in references):
            raise AppraisalError(f"market.evidence.{key} must reference source-bound claims")
    candidate = _object(manifest.get("candidate", {}), "candidate")
    for key in ("current_form", "pilot", "falsifier", "next_action"):
        _string(candidate.get(key), f"candidate.{key}")
    lenses = _object(manifest.get("lenses", {}), "lenses")
    for lens in LENSES:
        _string(lenses.get(lens, "unknown"), f"lenses.{lens}")

    missing = [key for key in ("buyer", "budget_owner", "verifier", "accepted_decision")
               if not isinstance(market.get(key), str) or not market[key].strip()
               or not market_evidence.get(key)]
    contradictory = sorted(k for k, stances in positions.items() if len(stances) == 2)
    challenges = [c for c in claim_rows if c["stance"] == "challenges"]
    support_sources = {c["source_id"] for c in claim_rows if c["stance"] == "supports"}
    independent = [c for c in challenges if c["source_id"] not in support_sources]
    if not independent:
        missing.append("independent_adverse_source")
    selected_id = manifest.get("strongest_counterexample_id")
    if selected_id is not None and selected_id not in {c["id"] for c in challenges}:
        raise AppraisalError("strongest_counterexample_id must name a challenging claim")
    selected = next((c for c in challenges if c["id"] == selected_id),
                    independent[0] if independent else (challenges[0] if challenges else None))
    # A declaration of a buyer/verifier in a manifest is not evidence of external
    # acceptance. The optimistic state only means the packet can be reviewed.
    status = "NEEDS_EVIDENCE" if missing or contradictory else "READY_FOR_HUMAN_REVIEW"
    if missing:
        next_action = "Find independent evidence for " + missing[0]
    elif contradictory:
        next_action = "Resolve conflicting evidence on " + contradictory[0]
    else:
        next_action = candidate["next_action"].strip()
    appraisal = {"version": VERSION, "question": question, "transaction": transaction,
                 "sources": source_rows, "claims": claim_rows,
                 "failure": {"layer": layer, "claim_ids": refs, "description": description},
                 "market": market, "candidate": candidate,
                 "lenses": {key: lenses.get(key, "unknown") for key in LENSES},
                 "contradictions": contradictory, "missing": missing,
                 "strongest_counterexample": selected,
                 "counterexample_selection": "human nomination; strength not independently established",
                 "status": status, "next_action": next_action,
                 "external_acceptance": "not tested", "consequence_class": "read_only"}
    body = {"manifest": manifest, "appraisal": appraisal}
    return {**body, "receipt_sha256": sha256(_canonical(body)).hexdigest()}


def verify(receipt: dict, source_root: str | Path) -> dict:
    receipt = _object(receipt, "receipt")
    if set(receipt) != {"manifest", "appraisal", "receipt_sha256"}:
        raise AppraisalError("receipt fields changed")
    regenerated = appraise(receipt["manifest"], source_root)
    if regenerated != receipt:
        raise AppraisalError("receipt or source binding changed")
    return {"verified": True, "receipt_sha256": receipt["receipt_sha256"],
            "scope": "source bytes and deterministic classification only; no external truth claim"}
