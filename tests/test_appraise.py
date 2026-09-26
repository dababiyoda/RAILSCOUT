"""Behavioral checks for evidence binding, refusal and replay."""

import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from railscout.appraise import AppraisalError, appraise, verify
from railscout.__main__ import main


class AppraisalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.a = b"Buyer has budget. Buyer needs verified proof.\n"
        self.b = b"An existing manual process may be sufficient.\n"
        (self.root / "a.txt").write_bytes(self.a)
        (self.root / "b.txt").write_bytes(self.b)
        def source(sid, file, raw):
            return {"id": sid, "path": file, "origin": f"local:{file}",
                    "collected_at": "2026-09-26T11:00:00Z", "rights": "test fixture",
                    "sha256": hashlib.sha256(raw).hexdigest()}
        self.manifest = {
            "question": "Is a proof workflow worth testing?",
            "transaction": "A buyer verifies proof before a payment decision",
            "sources": [source("buyer", "a.txt", self.a), source("manual", "b.txt", self.b)],
            "claims": [
                {"id": "a1", "source_id": "buyer", "topic": "budget", "assertion": "Buyer has budget",
                 "excerpt": "Buyer has budget.", "stance": "supports", "kind": "allegation"},
                {"id": "a2", "source_id": "buyer", "topic": "proof", "assertion": "Proof is needed",
                 "excerpt": "Buyer needs verified proof.", "stance": "supports", "kind": "allegation"},
                {"id": "b1", "source_id": "manual", "topic": "baseline", "assertion": "Manual may suffice",
                 "excerpt": "An existing manual process may be sufficient.", "stance": "challenges",
                 "kind": "allegation"}],
            "market": {"buyer": "Buyer", "budget_owner": "Buyer", "verifier": "Buyer",
                       "accepted_decision": "Proof accepted", "evidence": {
                           "buyer": ["a1"], "budget_owner": ["a1"], "verifier": ["a2"],
                           "accepted_decision": ["a2"]}},
            "failure": {"layer": "proof", "description": "Proof is missing", "claim_ids": ["a2"]},
            "candidate": {"current_form": "manual service", "pilot": "Compare manual and software",
                          "falsifier": "No time/cost or fidelity gain", "next_action": "Interview buyer"},
            "strongest_counterexample_id": "b1",
        }

    def test_receipt_checks_exact_bytes_without_claiming_external_truth(self):
        receipt = appraise(self.manifest, self.root)
        self.assertEqual(receipt["appraisal"]["status"], "READY_FOR_HUMAN_REVIEW")
        self.assertEqual(receipt["appraisal"]["external_acceptance"], "not tested")
        self.assertEqual(receipt["appraisal"]["claims"][0]["byte_start"], 0)
        self.assertTrue(verify(receipt, self.root)["verified"])
        self.assertEqual(receipt, appraise(self.manifest, self.root))
        receipt["appraisal"]["next_action"] = "Approve payment"
        with self.assertRaisesRegex(AppraisalError, "binding changed"):
            verify(receipt, self.root)

    def test_source_change_rejected_at_appraisal_and_replay(self):
        receipt = appraise(self.manifest, self.root)
        (self.root / "a.txt").write_bytes(self.a + b"changed\n")
        with self.assertRaisesRegex(AppraisalError, "source changed"):
            appraise(self.manifest, self.root)
        with self.assertRaisesRegex(AppraisalError, "source changed"):
            verify(receipt, self.root)

    def test_missing_market_evidence_or_conflict_abstains(self):
        self.manifest["market"]["evidence"].pop("budget_owner")
        self.assertEqual(appraise(self.manifest, self.root)["appraisal"]["status"], "NEEDS_EVIDENCE")
        self.manifest["market"]["evidence"]["budget_owner"] = ["a1"]
        self.manifest["claims"][2]["topic"] = "budget"
        result = appraise(self.manifest, self.root)["appraisal"]
        self.assertEqual(result["contradictions"], ["budget"])
        self.assertEqual(result["status"], "NEEDS_EVIDENCE")

    def test_same_source_adversary_does_not_pass_independence_gate(self):
        self.manifest["claims"][2]["source_id"] = "buyer"
        self.manifest["claims"][2]["excerpt"] = "Buyer has budget."
        result = appraise(self.manifest, self.root)["appraisal"]
        self.assertEqual(result["status"], "NEEDS_EVIDENCE")
        self.assertIn("independent_adverse_source", result["missing"])

    def test_source_timestamp_is_validated(self):
        self.manifest["sources"][0]["collected_at"] = "sometime"
        with self.assertRaisesRegex(AppraisalError, "timezone-aware"):
            appraise(self.manifest, self.root)

    def test_fabricated_quote_traversal_and_symlink_refused(self):
        self.manifest["claims"][0]["excerpt"] = "Not in the source."
        with self.assertRaisesRegex(AppraisalError, "missing or ambiguous"):
            appraise(self.manifest, self.root)
        self.manifest["claims"][0]["excerpt"] = "Buyer has budget."
        self.manifest["sources"][0]["path"] = "../a.txt"
        with self.assertRaisesRegex(AppraisalError, "relative and bounded"):
            appraise(self.manifest, self.root)
        self.manifest["sources"][0]["path"] = "link.txt"
        (self.root / "link.txt").symlink_to(self.root / "a.txt")
        with self.assertRaisesRegex(AppraisalError, "symlink source refused"):
            appraise(self.manifest, self.root)

    def test_command_produces_one_receipt_and_refuses_overwrite(self):
        input_path = self.root / "manifest.json"
        receipt_path = self.root / "receipt.json"
        input_path.write_text(json.dumps(self.manifest))
        self.assertEqual(main(["appraise", str(input_path), "--source-root", str(self.root),
                               "--output", str(receipt_path)]), 0)
        self.assertEqual(main(["verify", str(receipt_path), "--source-root", str(self.root)]), 0)
        self.assertEqual(main(["appraise", str(input_path), "--source-root", str(self.root),
                               "--output", str(receipt_path)]), 2)


if __name__ == "__main__":
    unittest.main()
