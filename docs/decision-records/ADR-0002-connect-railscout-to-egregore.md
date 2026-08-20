# ADR-0002: Connect RailScout to the UNIIMENTE Egregore

## Status

`RETAIN` as a doctrine and repository-connection decision. Production runtime integration remains deferred until contracts, tests, and execution evidence exist.

## Date

2026-08-19

## Intent references

- `INTENT-0002` - Local Recursive Founder-Intent Collaboration Protocol
- `INTENT-0003` - RailScout Egregore Connection
- `INTENT-0004` - Cumulative Project Workspace Corpus

## Decision level

Constitutional, because this affects cross-repository governance, organ identity, repository ownership, and the relationship between RailScout and the UNIIMENTE Kernel.

## Intended outcome

Make the RailScout repository understandable to the wider UNIIMENTE egregore while preserving the hierarchy: RailScout is an organ with local doctrine and operating records; the UNIIMENTE Kernel remains the constitutional control plane.

## Baseline

RailScout existed as a seed repository with minimal description. UNIIMENTE Kernel already had a RailScout organ concept, but RailScout's local repository was not fully captured as the organ's working home.

## Alternatives considered

| Alternative | Benefits | Liabilities | Disposition | Revival evidence |
|---|---|---|---|---|
| Do nothing | No extra files; no governance surface | Context loss persists; egregore cannot locate or understand RailScout local doctrine | Rejected | If RailScout remains only a private chat concept with no repository work |
| Put everything only in UNIIMENTE Kernel | One canonical governance surface | RailScout loses local operating memory; every local change becomes Kernel noise | Rejected | If RailScout is never developed as a separate organ repository |
| Give RailScout standalone governance independent of Kernel | Local autonomy and clarity | Authority drift; duplicated constitutional law; risk of self-authorized expansion | Rejected | None unless founder intentionally separates RailScout from UNIIMENTE |
| Connect RailScout as local organ repository subordinate to Kernel | Clear local doctrine; traceable founder intent; egregore knows where RailScout lives; authority hierarchy preserved | Requires maintaining local-to-Kernel boundary | Selected | Current best fit |
| Build runtime integration immediately | Faster toward product | Premature; no schemas/tests/runtime evidence yet | Deferred | Context-packet schema, tests, and first artifact loop exist |

## Required role review

### Founder-Intent Steward

Alfonso explicitly requested that the RailScout repository contain the conversation, connect to the egregore, and have its own recursive founder-intent collaboration protocol. The selected approach captures those intentions without converting them into unauthorized production authority.

### Systems Architect

The correct architecture is local organ repository plus central Kernel governance. RailScout owns doctrine, context packets, opportunity artifacts, and local decision records. Kernel owns constitutional governance, authority, identity, and cross-organ consequence gates.

### Adversarial Reviewer

Main risks: duplicated governance, local protocol interpreted as sovereignty, public repository revealing sensitive context, and polished doctrine being mistaken for runtime evidence. The design mitigates these by adding Kernel-control language, evidence-tier boundaries, and no production authority.

### Operator and Maintainer

Local files make the repo navigable: README, connection record, context packet, intent ledger, protocol, ADRs. This reduces future context loss and makes onboarding easier. Maintenance risk is bounded because the files are doctrine-level, not runtime-coupled.

### Evidence and Welfare Guardian

The update protects evidence integrity by explicitly marking founder statements as intent evidence, not external proof. It improves future participant welfare only indirectly by preventing hidden authority drift and preserving negative evidence requirements.

## Pass 1 - structural strengthening

### Advantages strengthened

1. **Local clarity** becomes a contributor and agent onboarding advantage: future work can inspect the RailScout repo directly rather than reconstructing intent from chat memory.
2. **Egregore connection** becomes a governance advantage: RailScout is visible to the Kernel without duplicating the Kernel.
3. **Local protocol** becomes a decision-quality advantage: material proposals require intent references, two upward passes, dissent preservation, rollback, and kill criteria.
4. **Cumulative context packet** becomes an evidence-preservation advantage: the conversation is preserved as source material with explicit evidence boundaries.

### Disadvantages redesigned

| ID | Downside | Response |
|---|---|---|
| D1 | Local RailScout protocol could be mistaken for constitutional authority. | Add explicit subordinate-to-Kernel rule in README, protocol, and egregore connection record. |
| D2 | Public repo could expose sensitive context. | Capture only this conversation's operating doctrine and avoid unrelated private details. |
| D3 | More documents could become governance theater. | Keep files minimal and directly tied to intent, protocol, connection, and first execution loop. |
| D4 | Cross-repo connection may drift. | Mirror the connection in UNIIMENTE Kernel organ registry and review on identity/governance changes. |
| D5 | Doctrine could be mistaken for runtime or market proof. | Mark current status as doctrine/workstation layer only; no runtime or external proof claimed. |

## Pass 2 - adversarial compounding

### Attack on Pass 1

- The subordinate-to-Kernel rule could still be ignored by future agents.
- Context packets may grow into dumps instead of decision-grade source records.
- The repo could accumulate doctrine faster than tests or real validation.
- Future PRs may bypass the local protocol unless a template/check is added.

### Downside conservation

| ID | Disposition | Rationale | Owner | Review trigger |
|---|---|---|---|---|
| D1 | `accepted` | Textual safeguards are sufficient for doctrine stage; runtime enforcement deferred. | Alfonso Lopez | First runtime or capability grant |
| D2 | `accepted` | Current packet excludes unrelated private material; public sensitivity remains a review risk. | Alfonso Lopez | Any broader corpus import |
| D3 | `accepted` | Minimal governance surface chosen; no additional bureaucracy installed. | Alfonso Lopez | More than three unused governance files or no executed loops |
| D4 | `experiment` | Kernel organ registry update tests the connection path. | Alfonso Lopez | Kernel branch review |
| D5 | `resolved` | README, context packet, and connection record all state doctrine-only status. | Alfonso Lopez | Any external claim or launch packet |

### Final strengthening

Keep the local connection as documentation and intent governance. Do not claim production integration. Add future enforcement only when RailScout has a runtime or PR workflow that needs it.

## Residual risks

| Risk | Mitigation | Owner | Review trigger |
|---|---|---|---|
| Repository grows as doctrine without proof | First build target must be a real artifact loop, not more philosophy | Alfonso Lopez | Next RailScout work session |
| Kernel and RailScout language diverge | Treat Kernel as controlling and review both branches together | Alfonso Lopez | Merge review or conflict |
| Future context import is incomplete | Preserve unavailable-source notes and mark missing evidence | Alfonso Lopez | Corpus import |

## Decision

`RETAIN`

Connect RailScout to the UNIIMENTE egregore as a local organ repository subordinate to the Kernel. Install and mark RailScout's own local recursive founder-intent collaboration protocol. Preserve this conversation as a context packet and intent records.

## Rollback

Revert this ADR, `docs/EGREGORE_CONNECTION.md`, context packet, intent records `INTENT-0002` through `INTENT-0004`, and the README egregore section. Keep `INTENT-0001` if workstation doctrine remains approved.

## Kill criteria

Kill or revise this connection if it causes RailScout to bypass Kernel authority, duplicate constitutional governance, claim production capabilities without evidence, or obscure Alfonso's final decision authority.
