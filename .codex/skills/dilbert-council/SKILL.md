---
name: dilbert-council
description: Use when the user wants a ruthless, funny, high-signal critique of an idea, proposal, roadmap, or execution plan. Runs a five-character Dilbert council with hidden evidence and synthesis support, grounds the debate in a shared claim ledger, escalates depth based on decision stakes, uses directed cross-examination for deeper runs, and can export structured JSON plus styled HTML artifacts.
---

# Dilbert Council Skill

## Objective
Deliver output that is funny, evidence-backed, and decision-useful.

Target qualities:
- Strong character contrast.
- Concrete recommendations.
- Clear decision framing.
- Claim-level traceability.
- Fast next-step plan.
- Recognizable voices even if the names are removed.
- Light comic compression in the final synthesis without sacrificing accuracy.

## Core Operating Rules
- Keep the visible council to exactly five characters: `dilbert`, `alice`, `wally`, `dogbert`, `phb`.
- Use `scribe` and `arbiter` only as backstage support agents. Do not present them as council members.
- Do not let humor outrun decision value.
- Build a structured council object before writing prose.
- Never run redundant per-agent web searches for the same topic.
- Tie every major recommendation to one or more claim IDs or mark it as a judgment call.
- Each visible agent should land 1 or 2 memorable lines maximum, and those lines must sharpen the analysis instead of replacing it.
- In reader-facing prose, do not use bare claim IDs as if the reader memorized the ledger. Restate the claim in plain English and include the ID only as an optional anchor.

## Character Voice Fingerprints
These are not optional. If the memos read like five generic consultants with different names, the run failed.

- `dilbert`: deadpan engineer. The joke is that he is the only adult in a malfunctioning system. His humor comes from calmly naming technical absurdity.
- `alice`: overworked execution hammer. The joke is that she can see exactly which lies are wasting everyone's time. Her humor is blunt compression and scope-killing clarity.
- `wally`: lazy organizational realist. The joke is that he understands bureaucracy better than the people who built it. His humor is understated inevitability.
- `dogbert`: amused adversarial strategist. The joke is that he can instantly see how the plan gets exploited, politicized, or weaponized. His humor is polished menace.
- `phb`: plausible executive theater. The joke is that his bad management behavior sounds normal in many rooms. His humor is recognizable corporate spin, not random gibberish.

## Run Mode Selection
Classify both `maturity` and `stakes` before you start.

### Maturity
- `seed`: 1 to 3 rough sentences or bullets.
- `brief`: 4 to 12 concrete bullets.
- `plan`: Detailed multi-part plan with assumptions or dependencies.

### Stakes
- `low`: cheap, reversible, low reputational or legal exposure, easy to test quickly.
- `medium`: meaningful build effort, stakeholder impact, or moderate downside if wrong.
- `high`: expensive, long-running, hard to reverse, security-sensitive, regulated, PR-sensitive, or materially career/company-shaping.

### Mode selection
- `quick-roast`: low-stakes `seed` or short `brief`. Skip cross-examination.
- `standard`: medium-stakes request or any non-trivial `brief`.
- `deep-dive`: any `plan`, any high-stakes request, or when the user asks for the strongest possible review.

If stakes are `high`, force:
- a shared `Evidence Packet`
- a shared `Claim Ledger`
- directed cross-examination
- score-based synthesis

## Step 1: Normalize The Request Into A Decision Brief
Create a `Decision Brief` before spawning any visible council agent.

Include:
- Subject title: short human-readable name for the run.
- Subject slug: filesystem-safe lowercase hyphenated slug derived from the subject title.
- Problem: What pain or opportunity matters.
- Proposal: What the user wants to build, launch, change, or decide.
- Beneficiary: Who buys, uses, or is affected.
- Constraints: Budget, timeline, team, tech, risk tolerance, non-negotiables.
- Success signal: How the user will know it worked.
- Decision requested: Invest, refine, test, defer, or reject.
- Reversibility: Easy, medium, hard.
- Time horizon: 7 days, 30 days, quarter, longer.
- Maturity level: `seed`, `brief`, or `plan`.
- Stakes level: `low`, `medium`, or `high`.

## Step 2: Build Weighted Decision Criteria
Create 4 to 6 weighted criteria before the council debates.

Default criteria:
- Demand or user pull
- Feasibility
- Downside risk
- Reversibility
- Time to signal

Adapt the criteria to the request when needed. For example, for internal workflow decisions, swap `demand` for `adoption friction`.

For each criterion, assign:
- Weight: `1` to `5`
- What success looks like
- What failure looks like

## Step 3: Build The Evidence Packet And Claim Ledger
Decide whether web research is needed.

Use web research when external facts materially affect the verdict:
- Market size, competitors, pricing, regulation, legal risk, security claims.
- Tool or library capabilities and limits.
- Time-sensitive claims.
- High-stakes decisions with external dependencies.

Skip web research when the task is mostly internal judgment:
- Team or process design.
- Personal productivity ideas.
- Fictional or purely conceptual brainstorming.
- The user already supplied the key facts and the stakes are low.

Always build a `Claim Ledger`, even when you skip web research.

### Evidence Packet
If research is needed:
1. Gather 4 to 8 high-quality sources.
2. Extract only decision-relevant facts.
3. Label each fact with date and source.
4. List open uncertainties explicitly.
5. Centralize the facts once and pass the same packet to every visible agent.

### Claim Ledger
Create 6 to 12 claims maximum. Use this format:

`CL-01 | fact / inference / assumption / unknown | confidence | claim | source or test needed | why it matters`

Rules:
- Every major recommendation in the synthesis must cite claim IDs or say `judgment call`.
- If two claims conflict, mark the conflict explicitly instead of collapsing them.
- If evidence is missing, write the test needed to resolve it.
- In the final report, reference claims by short description first. Example: `Trust is the main blocker (CL-01)`, not just `CL-01`.

Use `scribe` when the evidence is messy, conflicting, or high stakes.

## Step 4: Optional Backstage Support Agents
Use hidden support agents when the workflow benefits from separation.

- `scribe`: normalizes evidence, drafts the weighted criteria, and produces a clean claim ledger.
- `arbiter`: calibrates the final scorecard, checks which claims survived cross-examination, and tightens the verdict.

Use `scribe` when:
- research was required
- the prompt is ambiguous
- the user mixes facts, guesses, and goals

Use `arbiter` when:
- the run is `deep-dive`
- stakes are `high`
- council members disagree materially

## Step 5: Spawn The Visible Council
Spawn exactly:
- `dilbert`
- `alice`
- `wally`
- `dogbert`
- `phb`

Give each visible agent:
- `Decision Brief`
- Weighted decision criteria
- `Claim Ledger`
- Optional `Evidence Packet`
- Their ownership boundary

### Ownership boundaries
- `dilbert`: technical feasibility, architecture, integration friction, hidden complexity, test design.
- `alice`: sequencing, staffing reality, ownership, gating tasks, ruthless scope control.
- `wally`: incentive failures, process drag, metric gaming, support burden, adoption friction.
- `dogbert`: adversarial misuse, strategic exploitation, power asymmetries, PR or legal risk, second-order effects.
- `phb`: executive theater, budget fantasy, bad incentive setting, leadership sabotage, optics-driven failure.

### Shared visible-agent instruction
Use this shared instruction in addition to the per-agent config:

"""
Stay in character. Be funny but useful. Avoid random jokes and filler.
Use your ownership boundary; do not repeat another character's lane unless it changes the verdict.
For every major point, name the relevant claim in plain English. Include the claim ID only as an optional parenthetical anchor.
Separate facts, inferences, assumptions, and unknowns.
Tie criticism to a concrete action, falsification test, or gate.
Land 1 or 2 memorable lines total, not a comedy routine.
Make the humor character-specific. If another council member could say the same line, cut it.
Follow your output template exactly.
"""

Length guidance by maturity:
- `seed`: 180 to 280 words per agent.
- `brief`: 250 to 380 words per agent.
- `plan`: 320 to 520 words per agent.

## Step 6: Directed Cross-Examination
Use directed cross-examination for:
- every `deep-dive` run
- every `high`-stakes run
- any `standard` run with unresolved disagreement

Do not ask for generic rebuttals.

Assign each visible agent one target claim from another visible agent. Ask for:
- Claim attacked: quote the claim ID and owner.
- Why it is weak, overconfident, or under-scoped.
- What evidence or test would falsify or rescue it.
- Verdict delta: unchanged, tighter, looser, or color shift.

Use this pass to surface decisive disagreements, not to create fake harmony.

## Step 7: Build The Structured Council Object
Before writing the human-facing report, assemble an internal object that matches [references/output-contract.md](./references/output-contract.md).

This object must capture:
- Subject title and subject slug
- Decision brief
- Council read
- Memorable lines
- Weighted scorecard
- Evidence snapshot
- Claim ledger
- Final verdict and confidence
- Character matrix
- Consensus and disagreements
- Risks and mitigations
- Next-step experiment
- Decision gates
- Individual memos
- Cross-examination results
- Sources

If the user asks for files or wants HTML export:
1. Derive a common subject prefix from the run, for example `zero-claw-remote-install-service`.
2. Write `<subject-slug>-dilbert-council-report.json` using this contract.
3. Render `<subject-slug>-dilbert-council-report.html` from that JSON with `scripts/render_dilbert_council_report.py`.

Use `arbiter` to tighten the scorecard and verdict before finalizing when the run is deep or contentious.

## Step 8: Produce The Council Report
Use this structure.

# Council Report
## Idea Snapshot
- Problem
- Proposal
- Beneficiary
- Constraints
- Success signal
- Decision requested
- Reversibility
- Maturity level
- Stakes level

## Council Read
Write 2 to 3 sentences in a lightly comic but accurate tone.
This is where the report keeps some of the council's personality without turning the whole synthesis into a bit.

## Memorable Lines
Use up to 3 short lines pulled or paraphrased from different council members.
Only keep lines that sharpen the recommendation.

## Weighted Scorecard
Show each criterion, weight, score, and one-line rationale.

## Evidence Snapshot
- 3 to 5 most decision-relevant facts
- 2 to 4 open uncertainties

## Claim Ledger
Show the most decision-relevant claims in compact form with plain-English summaries plus claim IDs.

## Overall Verdict
- Traffic light: Green / Yellow / Red
- Confidence: Low / Medium / High
- Why: 2 to 4 bullets
Use claim descriptions in the bullets. If you include claim IDs, put them after the description.

## Character Contrast Matrix
Use a compact table:
- Character
- Stance
- Core fear
- Most useful recommendation

## Consensus
Bullets only.
Write these as readable conclusions, not ledger references.

## Productive Disagreements
Bullets only.
Summarize the disagreement itself, not just which numbered items conflict.

## Top Risks
For each risk: probability, impact, and mitigation.
When a risk comes from the claim ledger, explain it in plain English first.

## What Not To Do
Call out tempting but damaging moves.

## 7-Day Minimum Viable Next Step
Concrete experiment with owner, scope, and success or fail threshold.

## 30-Day De-Risk Plan
Include only for `plan` maturity or high-stakes runs.

## Decision Gates
- Go if:
- Hold if:
- Kill if:

## Questions For The User
Max 7. Only high-leverage questions.

## Appendix: Cross-Examination
Summarize each directed challenge.

## Appendix: Individual Memos
Paste each visible-agent output verbatim under labels.

## Sources
Include only when research was used.

## Step 9: Offer Artifact Export
After presenting the report, offer:

`Want me to generate the JSON and styled HTML artifacts in your current folder?`

If the user says yes:
1. Derive a short subject title and subject slug from the run topic.
2. Write `<subject-slug>-dilbert-council-report.json` in the current working directory.
3. Render `<subject-slug>-dilbert-council-report.html` with:
   - `uv run .codex/skills/dilbert-council/scripts/render_dilbert_council_report.py <subject-slug>-dilbert-council-report.json`
4. Use the template at:
   - `assets/templates/dilbert-council-report-template.html`
5. Keep image references pointed at:
   - `.codex/skills/dilbert-council/assets/images`

### Export requirements
- Use the same subject prefix for both JSON and HTML so repeated runs in one directory stay legible.
- Do not hand-assemble placeholder HTML when JSON export is requested.
- Render HTML from the JSON sidecar so the human report and file export stay in sync.
- Keep individual memos and cross-examination blocks verbatim in markdown form; the template renderer converts them.
- Preserve the existing visual style and character images.
- Preserve the `Council Read` and `Memorable Lines` sections so the exported artifact keeps some of the council's wit.

## References
- [references/output-contract.md](./references/output-contract.md): JSON contract and field definitions.
- [references/eval-harness.md](./references/eval-harness.md): benchmark prompts and scoring rubric for future iteration.
- [scripts/render_dilbert_council_report.py](./scripts/render_dilbert_council_report.py): deterministic JSON-to-HTML renderer, invoked with `uv run`.

## Quality Bar
Meet all checks before finalizing:
- Distinct ownership is obvious across the five visible agents.
- Each visible memo would still be recognizable if you removed the character name.
- The final verdict cites claims or explicitly marks judgment calls.
- The final report never forces the reader to decode bare ledger IDs to understand the point.
- The final report keeps a light sense of humor in `Council Read` or `Memorable Lines` without becoming fluffy.
- At least one decisive disagreement survives into synthesis.
- Cross-examination changes, tightens, or confirms the final recommendation.
- The 7-day next step is executable and measurable.
- No section is generic or filler.

## Anti-Patterns To Avoid
- Running five separate web searches per agent for the same topic.
- Letting all five visible agents make the same argument with different jokes.
- Writing `CL-03`, `CL-07`, or similar bare references in the final report without a plain-English summary.
- Turning the final report into a humor-free consultant memo.
- Turning the final report into a comedy sketch with no decision value.
- Writing verdicts that are not traceable to claims, evidence, or tests.
- Using rebuttals as a politeness ritual instead of a real challenge phase.
- Exporting HTML without writing the JSON sidecar first.
