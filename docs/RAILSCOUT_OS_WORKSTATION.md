# RailScout OS Workstation Build Specification

This document preserves the RailScout OS workstation intent from the 2026-08-19 LIVE PLAYER conversation.

## Core premise

RailScout OS is not just a Notion workspace. It is a governed app/tool-orchestrating operating system where Notion is the command memory, connected apps are specialized actuators, and Governor Scheduled Runs decide when and how tools are used.

## Control architecture

| Layer | Function |
|---|---|
| Notion | Command memory / control plane |
| Governor Scheduled Runs | Heartbeat and recurring system-improvement cadence |
| Tool/App Registry | Nervous system for app permissions, use cases, risks, fallbacks, and expected outputs |
| Connected apps/tools | Bounded execution limbs |
| Cadence Run Notes | Audit trail |
| Decision Log | Judgment memory |
| Evidence Notes | Proof layer |
| Terminal Case Log | Prevents zombie work |
| Duplicate / Revival Queue | Prevents repeated waste |
| Doctrine / Templates | Repeatability layer |

## Required root rule

Everything must live under the existing shared `RailScout OS` root page so ChatGPT/RailScout can read, write, edit, create, and update records through inherited permissions.

Do not create side-canon pages. Do not rename core databases.

## Existing databases

The first two databases already exist:

1. `Entity Registry`
2. `Opportunity Ledger`

## Databases to create in order

1. `Scoreboard Snapshots`
2. `Rank Entries`
3. `Assumption Registry`
4. `Blockers / Constraints`
5. `Validation Targets`
6. `Evidence Notes`
7. `Decision Log`
8. `Terminal Case Log`
9. `Cadence Run Notes`
10. `Tool / App / Skill Lessons`
11. `Sticky Notes for Alfonso`
12. `Duplicate / Revival Queue`
13. `Governor Scheduled Runs`
14. `Doctrine / Templates`

## Dashboards to create last

1. `Start Here`
2. `Command Center`
3. `Governor Scheduled Runs Dashboard`
4. `FIND Dashboard`
5. `IMPROVE Dashboard`
6. `GOV-BUILD Dashboard`
7. `Boundary Guardian Dashboard`
8. `Maintenance Dashboard`

## Governor Scheduled Runs database

### Purpose

Make RailScout self-improving, self-sustaining, future-proof, and continuity-preserving.

### Required properties

- `Scheduled Run` — Title
- `Cadence Type` — Select: `FIND`, `IMPROVE`, `GOV-BUILD`, `Boundary Guardian`, `Maintenance`, `Self-Improvement`, `Continuity Audit`
- `Frequency` — Select: `Daily`, `Weekly`, `Bi-Weekly`, `Monthly`, `Quarterly`, `Ad Hoc`
- `Next Run` — Date
- `Last Run` — Date
- `Run Owner` — Person
- `Status` — Select: `Active`, `Paused`, `Retired`
- `Required Inputs` — Text
- `Required Outputs` — Text
- `Linked Cadence Runs` — Relation to `Cadence Run Notes`
- `Success Criteria` — Text
- `Self-Improvement Prompt` — Text
- `Continuity Check` — Checkbox
- `Dashboard Link` — URL or Text

### Seed records

1. `Weekly FIND Run`
   - Frequency: Weekly
   - Required Outputs: one winner, duplicates flagged, evidence gaps, next validation targets
2. `Weekly IMPROVE Run`
   - Frequency: Weekly
   - Required Outputs: blocked/improving items diagnosed, failed validations extracted, redesign decisions logged
3. `Weekly GOV-BUILD Run`
   - Frequency: Weekly
   - Required Outputs: scoreboard snapshot, rank entries, governance decisions
4. `Weekly Boundary Guardian Run`
   - Frequency: Weekly
   - Required Outputs: duplicate review, revival review, staleness review, archive hygiene
5. `Monthly Continuity Audit`
   - Frequency: Monthly
   - Required Outputs: schema drift check, orphan records, broken relations, stale assumptions, missing decision logs
6. `Monthly Self-Improvement Run`
   - Frequency: Monthly
   - Required Outputs: tool lessons updated, sticky notes resolved, system improvements proposed, dashboards cleaned

## Start Here dashboard rule

`Start Here` must become the AI operator entry page. It should contain:

- link to `Command Center`;
- link to `Governor Scheduled Runs Dashboard`;
- link to `FIND`, `IMPROVE`, `GOV-BUILD`, `Boundary Guardian`, and `Maintenance` dashboards;
- linked views of active scheduled runs, due next actions, open critical blockers, stale opportunities, and Gov/Build-ready opportunities;
- short operating protocol:

> Start at Command Center. Check due Governor Scheduled Runs. Create or update a Cadence Run Note. Update related opportunities, evidence, validations, assumptions, blockers, and decisions. Close with Continuity Notes.

## Required relation map

After all databases are created, add relations and rollups so RailScout can navigate from any opportunity to:

- evidence;
- validations;
- assumptions;
- blockers;
- decisions;
- cadence runs;
- terminal cases;
- rank history;
- duplicate/revival status;
- scheduled runs that affect it;
- tools/apps used to produce or update it.

## Dashboard completion questions

The workspace is not finished until an AI operator can answer these questions from dashboards without manual searching:

1. What should be worked on next?
2. What is stale?
3. What is blocked?
4. What is ready for GOV-BUILD?
5. What was killed, parked, or merged, and why?
6. What assumptions remain dangerous?
7. What proof exists?
8. What scheduled run is due next?
9. What did the system learn from the last run?
10. What must be improved in the workspace itself?

## Tool/App Registry

Add a `Tool / App Registry` database or upgrade `Tool / App / Skill Lessons` into a full registry.

### Purpose

Define how RailScout uses every connected app/tool as part of scheduled runs, validation workflows, evidence gathering, communication, artifact creation, and self-improvement.

### Required properties

- `Tool / App` — Title
- `Category` — Select: `Memory`, `Search`, `Execution`, `Communication`, `Scheduling`, `Analysis`, `Artifact Creation`, `Automation`, `Finance`, `Legal`, `Design`, `Data`
- `Primary Use Case` — Text
- `Allowed Actions` — Multi-select: `Read`, `Search`, `Create`, `Update`, `Delete`, `Send`, `Schedule`, `Analyze`, `Export`
- `Forbidden / Caution Actions` — Text
- `Required Inputs` — Text
- `Expected Outputs` — Text
- `Connected Databases` — Relation to relevant Notion databases
- `Used By Scheduled Runs` — Relation to `Governor Scheduled Runs`
- `Failure Modes` — Text
- `Fallback Tool` — Text or Relation
- `Last Successful Use` — Date
- `Last Failure` — Date
- `Status` — Select: `Active`, `Limited`, `Broken`, `Deprecated`, `Needs Setup`
- `Operator Notes` — Text
- `Permission Risk` — Select: `Low`, `Medium`, `High`
- `Human Approval Required` — Checkbox

### Required relations

- `Tool / App Registry` ↔ `Governor Scheduled Runs`
- `Tool / App Registry` ↔ `Cadence Run Notes`
- `Tool / App Registry` ↔ `Tool Lessons`
- `Tool / App Registry` ↔ `Doctrine / Templates`
- `Tool / App Registry` ↔ `Evidence Notes` when the tool produced evidence
- `Tool / App Registry` ↔ `Decision Log` when the tool influenced a decision

No app/tool should be used randomly. Every use must be tied to a scheduled run, validation target, opportunity, evidence note, blocker, decision, maintenance task, or terminal-case update.

## App/tool role model

RailScout routes apps/tools into three roles:

### Sense

Tools that detect reality.

Examples: web search, Gmail, Google Drive, file search, calendar, CRM/search tools if connected.

Question answered: what changed outside or inside the system?

### Decide

Tools that structure judgment.

Examples: Notion databases, spreadsheets, scoring models, decision logs, evidence registries.

Question answered: what matters, what wins, what dies, what needs proof?

### Act

Tools that produce or change something.

Examples: Gmail drafts/sends, Calendar scheduling, Docs, Slides, PDFs, Notion updates, automations, design/image tools, GitHub issues/PRs.

Question answered: what action should be executed now?

RailScout must not act before sensing and deciding unless a pre-authorized emergency/maintenance path exists.

## Core loop

```text
SENSE -> COMPARE -> SCORE -> DECIDE -> ACT -> LOG -> IMPROVE
```

Mapped to apps:

```text
Search/Gmail/Drive/Web -> Notion/Sheets -> Scoreboard -> Decision Log -> Apps/Artifacts -> Cadence Run Notes -> Tool Lessons
```

## Hard residue rule

RailScout should never use a tool without producing at least one of these records:

- Evidence Note
- Decision Log entry
- Cadence Run Note
- Validation Target
- Blocker / Constraint
- Tool Lesson
- Opportunity update
- Terminal Case update
- Scheduled Run update

Otherwise the work evaporates and does not compound.
