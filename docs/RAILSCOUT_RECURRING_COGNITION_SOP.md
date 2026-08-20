# RailScout Recurring Cognition SOP

Status: production-line design, not proof of live execution  
Owner: Alfonso Lopez  
Created: 2026-08-19  
Primary use: configure and govern RailScout as a recurring scheduled Workspace Agent with persistent estimate, assumption, evidence, belief, run-note, and drift records.

## 1. Product facts that constrain implementation

This SOP is constrained by official OpenAI documentation inspected on 2026-08-19.

1. ChatGPT Workspace Agents are intended for repeatable tasks and workflows. They can use tools, apps, custom MCPs, skills, and files in the agent builder. They can run in ChatGPT, can be connected to Slack, can run on a schedule, and can be triggered through an API where configured.
   - Source: OpenAI Help Center, `ChatGPT Workspace Agents for Enterprise and Business`, https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business
2. Workspace Agent schedules are configured from the ChatGPT channel page by selecting Add schedule, choosing channel, schedule type, frequency, additional instructions, and Add schedule.
   - Source: OpenAI Help Center, `ChatGPT Workspace Agents for Enterprise and Business`.
3. Workspace Agent changes require update/publish behavior before they are live.
   - Source: OpenAI Help Center, `ChatGPT Workspace Agents for Enterprise and Business`.
4. Scheduled Tasks in ChatGPT can be one-off or recurring and can monitor for meaningful changes, but tasks cannot run more than once per hour. Active task limits depend on plan.
   - Source: OpenAI Help Center, `Scheduled Tasks in ChatGPT`, https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
5. Projects can keep related chats, files, and instructions together; project memory can draw context from the same project where enabled.
   - Source: OpenAI Help Center, `Projects in ChatGPT`, https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt-496

Design implication: recurring cognition is feasible as a Workspace Agent design, but continuity must be stored in explicit ledgers. Memory helps with context. Memory is not the canonical operating database.

## 2. Agent B: Recurring Cognition Operator

Agent B is the bounded scheduled worker role inside RailScout.

### Job

Agent B maintains the recurring cognitive loop:

- check current state;
- update Fermi estimates;
- update Bayesian beliefs;
- route mental models to the problem;
- preserve evidence and assumptions;
- detect drift;
- leave handoffs;
- escalate only when authority, money, external effects, or doctrine are implicated.

### Non-job

Agent B does not:

- publish;
- contact people;
- spend money;
- sign contracts;
- change legal obligations;
- grant itself authority;
- override Kernel governance;
- convert founder aspiration into executable authority;
- treat memory or estimates as proof.

## 3. Canonical stores

RailScout must maintain these stores in a durable system of record.

### 3.1 Estimate Ledger

Purpose: persistent, versioned Fermi estimates.

Required fields:

- estimate ID;
- target quantity;
- domain;
- formula;
- factor values with low/base/high values and units;
- current estimate;
- prior estimate;
- delta;
- confidence;
- evidence added;
- evidence removed or downgraded;
- assumptions changed;
- decision impact;
- status;
- next review trigger.

### 3.2 Assumption Ledger

Purpose: factor-level assumptions powering estimates and strategy decisions.

Required fields:

- assumption ID;
- assumption statement;
- linked estimate or decision;
- source;
- confidence;
- falsification condition;
- owner;
- next review trigger.

### 3.3 Evidence Ledger

Purpose: separate observation, inference, missing proof, and next verification step.

Evidence hierarchy:

1. statutes, regulations, court records, official datasets, procurement records, standards, audited filings;
2. company filings, earnings transcripts, patents, grant databases, official technical documentation;
3. peer-reviewed research and academic sources;
4. consulting and industry reports as signal maps, not proof;
5. media, blogs, social signals, anecdotes.

### 3.4 Bayesian Belief Register

Purpose: track confidence updates explicitly.

Required fields:

- belief ID;
- claim;
- prior confidence;
- evidence event;
- likelihood ratio or qualitative update;
- posterior confidence;
- decision effect;
- dissent or counterevidence;
- next review trigger.

### 3.5 Run Notes

Purpose: make scheduled runs cumulative.

Each run note must include:

- run type;
- sources checked;
- unavailable sources;
- estimates updated;
- estimates intentionally unchanged;
- evidence that moved confidence;
- contradiction found;
- broken source or tool;
- next-run instruction;
- one thing not to repeat.

### 3.6 Drift and Incident Log

Purpose: prevent one bad run from corrupting the system.

Log:

- missing input;
- malformed estimate;
- unsupported claim;
- stale memory use;
- major unexplained delta;
- contradiction;
- tool failure;
- broken schedule;
- output-format failure;
- authority conflict.

## 4. Mental-model router

Use mental models only when they change the decision.

| Trigger | Model | Output |
|---|---|---|
| Unknown quantity | Fermi estimate | Low/base/high estimate and sensitive factor |
| New evidence changes confidence | Bayesian update | Prior, evidence, posterior, action change |
| Too many options | 80/20 | Dominant few variables |
| Fragile idea | Inversion | Failure modes and kill criteria |
| Confusing surface issue | First principles | Buyer, payer, proof, law, cash, workflow |
| Constraint blocks path | Constraint-to-advantage | Moat, learning loop, redesign, or stop signal |
| Uneven upside | Power law | Tail opportunity and bottleneck |
| Uncertain future path | Optionality | Reversible staged move |
| Goal clear, path unclear | Backcast GPS | Destination, nodes, current gate, next action |
| Multiple strategies | Strategic tree search | Baseline, do-nothing, fastest, resilient, hybrid |
| Market-structure question | Control-layer analysis | Proof, eligibility, routing, settlement, gatekeeper |
| Robustness needed | Red team | Strongest counterexample |
| Long-run effects matter | Consequence map | First-, second-, third-order effects |
| Irreversible action | Regret test | No-go or reversible alternative |

## 5. Fermi estimate engine

Every Fermi estimate follows this sequence:

1. Define the target quantity precisely.
2. Split the target into drivers.
3. Assign low/base/high values with units.
4. Anchor factors in the strongest available sources.
5. Calculate the range.
6. Identify the most sensitive factor.
7. Name the cheapest decisive evidence.
8. Decide what action changes.
9. Store the snapshot.
10. On future runs, update only affected factors.

Generic opportunity value formula:

`opportunity value = reachable buyers x acute-pain rate x conversion rate x annual contract value x gross margin x retention duration x execution probability`

A Fermi estimate must end in one of:

- verify factor;
- validate buyer;
- price test;
- kill;
- park;
- build small;
- escalate to weekly governance.

If it does not change a decision, it is decorative and should not be preserved as progress.

## 6. Bayesian update rule

When evidence arrives:

1. What was the prior belief?
2. How expected was this evidence if the belief were true?
3. How expected was this evidence if the belief were false?
4. Does confidence move up, down, or stay flat?
5. What decision changes?

Numeric form:

`posterior odds = prior odds x likelihood ratio`

Qualitative updates allowed:

- strong upward;
- moderate upward;
- weak upward;
- neutral;
- weak downward;
- moderate downward;
- strong downward.

## 7. Cadence architecture

### 7.1 3-hour FIND / Signal Delta

Purpose: keep the opportunity field fresh without rebuilding the whole system every run.

Sequence:

1. Load latest run note, estimate ledger, assumption ledger, evidence ledger, and scoreboard.
2. Check high-signal sources only.
3. Identify new regulatory, market, procurement, funding, litigation, technical, or operational signals.
4. Reject noise and duplicates.
5. Update only affected estimates and beliefs.
6. Create candidate opportunities only when the signal implies a broken proof, trust, eligibility, routing, settlement, compliance, or coordination rail.
7. Leave a handoff for Daily IMPROVE.

### 7.2 Daily IMPROVE / Reconciliation

Purpose: turn signals into better decisions.

Sequence:

1. Audit recent FIND outputs.
2. Detect duplicates and repeated weak ideas.
3. Run failure classification: market, configuration, evidence, timing, execution.
4. Apply mental models where they change the business.
5. Update Fermi estimates and Bayesian beliefs.
6. Improve one winner and one salvageable loser.
7. Keep true dead ideas dead.
8. Leave input for Weekly GOV / BUILD.

### 7.3 Weekly GOV / BUILD

Purpose: protect against beautiful nonsense and produce launch-ready packages.

Sequence:

1. Audit the full production line.
2. Re-rank the official scoreboard.
3. Promote, demote, merge, park, revive, or kill ideas.
4. Select one build priority without hedging.
5. Produce a launch packet: thesis, buyer, payer, gatekeeper, offer, pricing, proof artifact, validation plan, outreach, evidence packet, risk analysis, control-rail path, 30-day plan, kill criteria.
6. Audit RailScout itself: tool use, evidence discipline, run-note quality, drift, duplication, and founder-bottleneck reduction.

### 7.4 Monthly Constitutional Review

Purpose: prevent recurring cognition from becoming unauthorized authority.

Sequence:

1. Review all capability requests.
2. Check for unauthorized external effects.
3. Check whether memory was treated as proof.
4. Check whether estimates affected decisions without evidence.
5. Regress or freeze any capability that drifted.

## 8. Run contract

Every scheduled run must:

1. Identify the run type.
2. Retrieve canonical state before reasoning.
3. State unavailable sources.
4. Separate observations, inferences, and proposals.
5. Use mental models only where they change a decision.
6. Update ledgers or produce proposed ledger updates.
7. Preserve negative evidence and broken runs.
8. End with a decision label and next action.

Allowed decision labels:

- Build now
- Validate first
- Research more
- Park
- Kill
- Pivot
- Revive
- Needs founder decision

## 9. Failure handling

If a run breaks:

1. Do not overwrite the prior accepted estimate.
2. Mark the run incomplete.
3. Preserve partial output in the Drift and Incident Log.
4. State exact failure.
5. Revert operational decisions to the last stable run.
6. Create one next-run repair instruction.
7. Escalate to Alfonso only if authority, money, legal exposure, external effects, or core doctrine are implicated.

If inputs are missing:

- use the prior estimate as prior, not as truth;
- do not create fake freshness;
- mark the factor stale;
- identify cheapest decisive evidence.

If stale memory appears:

- stop the run;
- reload dated ledgers;
- prefer newest canonical source over older memory;
- preserve older memory only as historical context;
- log the drift event.

## 10. Anti-stagnation rule

Every useful run must do at least one of:

- add evidence;
- update estimate;
- revise confidence;
- challenge assumption;
- kill weak idea;
- strengthen promising idea;
- merge duplicate;
- clean workspace;
- sharpen next validation action;
- log a system defect.

If none occurs, the run must state:

`No material movement. Do not treat this run as progress.`

## 11. First-run bootstrap

The first production run must create baseline state:

1. Estimate Ledger v0.
2. Assumption Ledger v0.
3. Evidence Ledger v0.
4. Bayesian Belief Register v0.
5. Current Opportunity Scoreboard v0.
6. Run Note v0.
7. Drift and Incident Log v0.
8. One selected Single Bottleneck Metric.

Initial Single Bottleneck Metric:

`validated opportunity conversion`: number of opportunities that produce paid or commitment-based validation within 14 days.

Secondary metric:

`estimate usefulness`: percentage of estimate updates that change a decision, validation action, or build/park/kill label.

## 12. Activation checklist

- [ ] Choose the canonical system of record.
- [ ] Confirm app/tool permissions.
- [ ] Publish or update the Workspace Agent.
- [ ] Add schedules only after agent configuration is live.
- [ ] Run one manual dry run for each cadence.
- [ ] Verify outputs are written to correct store.
- [ ] Confirm fail-closed behavior when sources are missing.
- [ ] Confirm memory is not treated as proof.
- [ ] Confirm no external action can occur without current authority.

## 13. Local invariant

RailScout may compound cognition. It may not compound unauthorized action.
