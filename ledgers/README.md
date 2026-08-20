# RailScout Ledgers

Status: templates for the first manual dry run  
Owner: Alfonso Lopez  
Created: 2026-08-19

RailScout ledgers are the durable memory of the refinery. Model memory can help retrieve context, but these ledgers are the operating record.

## 1. Estimate Ledger

| estimate_id | domain | target_quantity | formula | factor_values_low_base_high | current_estimate | prior_estimate | delta | confidence | evidence_added | evidence_removed | assumptions_changed | decision_impact | status | next_review |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EST-000 | baseline | TBD | TBD | TBD | TBD | none | none | unknown | none | none | none | none | needs_evidence | first dry run |

Allowed status values:

- active
- watch
- stale
- superseded
- invalidated
- needs_evidence

## 2. Assumption Ledger

| assumption_id | statement | linked_estimate_or_decision | source | confidence | falsification_condition | owner | next_review |
|---|---|---|---|---|---|---|---|
| ASM-000 | TBD | TBD | none | unknown | TBD | Alfonso | first dry run |

## 3. Evidence Ledger

| evidence_id | claim_or_signal | type | source | evidence_tier | date_checked | finding | limitation | linked_decision | next_verification_step |
|---|---|---|---|---|---|---|---|---|---|
| EVD-000 | Workspace Agents support repeatable workflows and schedules where configured | external_evidence | OpenAI Help Center | official product documentation | 2026-08-19 | supports recurring agent design | exact workspace permissions still must be checked | Agent B design | confirm workspace agent configuration in account |

Evidence types:

- observation
- inference
- proposal
- aspiration
- active_requirement
- constitutional_invariant
- implementation
- simulation
- generated_artifact
- historical_artifact
- external_evidence
- unresolved_claim

Evidence tiers:

1. official legal, regulatory, standards, audited, or government source;
2. official company/product documentation or filings;
3. peer-reviewed/academic source;
4. consulting or industry report;
5. media, blog, social, anecdote;
6. model output only.

## 4. Bayesian Belief Register

| belief_id | claim | prior | evidence_event | likelihood_ratio_or_qualitative_update | posterior | decision_effect | dissent | next_review |
|---|---|---|---|---|---|---|---|---|
| BEL-000 | RailScout can be configured into a recurring cognition loop | medium | OpenAI docs confirm Workspace Agent schedules and repeatable workflows | moderate upward | medium-high, pending account setup | proceed to manual dry run and config check | live run not yet proven | first dry run |

## 5. Run Notes

| run_id | run_type | date | sources_checked | unavailable_sources | estimates_updated | estimates_unchanged | evidence_that_moved_confidence | contradictions | broken_tools_or_sources | next_run_instruction | do_not_repeat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| RUN-000 | baseline | 2026-08-19 | RAILSCOUT repo initialization | live Workspace Agent config not checked | none | none | OpenAI Help Center product facts | none | none | create first real baseline | do not treat repo docs as proof of live execution |

## 6. Drift and Incident Log

| incident_id | date | run_id | incident_type | description | affected_records | containment_action | owner | review_trigger |
|---|---|---|---|---|---|---|---|---|
| DFT-000 | 2026-08-19 | conversation | stale_memory_risk | Assistant responses felt generic and out of chronological order | founder trust, future simulation, memory hierarchy | install dated founder-intent ledger and stale-memory rule | Alfonso / RailScout | any future stale response |

Incident types:

- missing_input
- malformed_estimate
- unsupported_claim
- stale_memory_use
- major_unexplained_delta
- contradiction
- tool_failure
- broken_schedule
- output_format_failure
- authority_conflict
- external_effect_attempt

## 7. Opportunity Scoreboard

| opportunity_id | title | status | buyer | payer | gatekeeper | pain | evidence_confidence | validation_path | control_layer | next_action | kill_criteria |
|---|---|---|---|---|---|---|---|---|---|---|---|
| OPP-000 | TBD | needs_evidence | TBD | TBD | TBD | TBD | unknown | TBD | TBD | first dry run | no buyer/payer/proof path |

Allowed opportunity status values:

- raw
- researching
- validate_first
- build_now
- parked
- killed
- pivot
- revived
- launched
- superseded

## 8. Rule

A ledger update is only progress if it improves decision quality, evidence quality, validation speed, founder leverage, or system reliability.
