# RailScout

RailScout is the research and evidence organ of UNIIMENTE. The executable v0
appraises a **provided** opportunity packet. It checks that every quoted passage
exists in unchanged source bytes, retains the contrary case, and refuses to call
an opportunity ready for review when the buyer, budget, verifier or decision is
unsupported. It does not discover markets or authenticate external claims.

## Run the bounded source appraiser

Requires Python 3.11+; uses only the standard library.

```bash
python -m railscout appraise examples/project-source-packet/manifest.json \
  --source-root examples/project-source-packet --output /tmp/railscout-receipt.json
python -m railscout verify /tmp/railscout-receipt.json \
  --source-root examples/project-source-packet
python -m unittest discover -s tests -v
```

The checked-in `examples/project-source-packet/receipt.json` is a deterministic
demonstration against three **real project source excerpts**. It finds a direct
conflict between an older custom-substrate claim and the current agent rule,
then returns `NEEDS_EVIDENCE` because no actual buyer, budget, verifier or
accepted transaction is present. It is not a market validation or proof of a
GREG mission. The CLI refuses to overwrite a receipt. Verification re-reads
the source files and recomputes the entire result; any edited source or
altered receipt fails. Claim selection and assessment of the external world's
truth remain human responsibilities.

The format is visible in `examples/project-source-packet/manifest.json`:
source IDs, relative paths, expected SHA-256 hashes, origin and rights; quoted
claims with stance and topic; market fields with references to claims; a
bounded candidate, falsifier and next action. One separately sourced challenge
is required before the optimistic `READY_FOR_HUMAN_REVIEW` status. That status
still means only that a human can inspect the packet, never that a buyer or
external institution has accepted it.

## GREG boundary and build order

See [quoted founder intent and executable acceptance](docs/FOUNDER_SOURCE_AND_CODED_SLICE_2026-09-26.md),
[RailScout implementation issue #8](https://github.com/dababiyoda/RAILSCOUT/issues/8)
and [Kernel coordination #117](https://github.com/dababiyoda/uniimente-kernel/issues/117).
This Python entrypoint can be invoked by a future bounded adapter. No adapter
is registered in the current Kernel/GREG body from this RailScout branch;
GREG cannot yet invoke the function as a signed mission. The Kernel remains
the sole authority, grant, budget, evidence and consequence owner.

The next integration work should consume the current `greg.capabilities`
broker and journal on the reviewed product branch, apply read roots, receipt
appraisal, and return control to the original mission. Verify the integration
end to end; do not count this repository's CLI test as a durable GREG closure.
