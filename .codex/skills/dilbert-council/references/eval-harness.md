# Dilbert Council Eval Harness

Use this reference after meaningful revisions to the skill.

The goal is not to check whether the council sounds funny. The goal is to check whether it produces differentiated, evidence-backed, decision-useful output.

## Quick Rubric
Score each category `0`, `1`, or `2`.

- `Problem framing`: Did the council identify the real decision, not just restate the prompt?
- `Claim quality`: Are major synthesis points traceable to claim IDs, evidence, or explicit tests?
- `Role separation`: Do the five visible agents own distinct lanes, or are they repeating each other?
- `Cross-examination quality`: Does the challenge phase attack specific claims and change calibration?
- `Decision usefulness`: Is the 7-day next step concrete, measurable, and falsifiable?
- `Calibration`: Does the traffic-light verdict match the evidence strength and scorecard?

Interpretation:
- `10-12`: strong run
- `7-9`: useful but still leaking redundancy or weak grounding
- `0-6`: the skill is performing as themed commentary, not a decision system

## Quick Fail Conditions
Fail the run immediately if any of these happen:
- No shared claim ledger
- No substantive disagreement in a deep-dive run
- The next-step plan has no pass or fail threshold
- At least two visible agents are making the same argument with different jokes
- The final verdict ignores obvious uncertainty
- The exported JSON fails strict rendering validation

## Export Regression Check
After any meaningful skill or renderer revision, render at least one completed JSON artifact with strict validation:

`uv run .codex/skills/dilbert-council/scripts/render_dilbert_council_report.py --strict <subject-slug>-dilbert-council-report.json`

Expected signal:
- No missing required top-level fields.
- Five visible memos are present.
- The character matrix includes all five visible personas.
- Scorecard has 4 to 6 criteria.
- Claim ledger has 6 to 12 claims.
- Research-heavy runs include source hierarchy.
- Research-report critiques include a fact / inference / unknown split.
- AI product, model, API, or platform reviews include an availability matrix when access or rollout affects the verdict.
- Yellow verdicts caused by unproven workflow value include a benchmark test plan.
- 7-day plan has owner, scope, success threshold, and fail threshold.
- Deep-dive or high-stakes runs include cross-examination and verdict sensitivity.
- Sources are clickable when they use http or https URLs.
- Character images render when the HTML file is opened from a subfolder.

## Benchmark Prompts

### 1. Low-stakes consumer idea
`Use dilbert-council quick-roast this idea: "AI meal planner for families."`

Expected signal:
- Fast, funny critique
- No unnecessary research
- One crisp next-step test

### 2. Internal process change
`Use dilbert-council standard review this idea: "Replace weekly standups with async status updates and one live blocker meeting."`

Expected signal:
- Wally and PHB should matter more than Dogbert
- Adoption friction should appear in the criteria

### 3. Security-sensitive service
`Use dilbert-council deep-dive this plan: "Remote install and manage always-on AI agents on customer-owned VPS machines." Do web research first.`

Expected signal:
- High-stakes escalation
- Evidence packet and claim ledger
- Dogbert and Dilbert should carry real weight
- Cross-examination should tighten the verdict

### 4. Regulated workflow
`Use dilbert-council deep-dive this proposal: "AI assistant for insurance claim triage with automatic denial recommendations."`

Expected signal:
- High-stakes escalation even if the prompt is short
- Strong legal, PR, and reversibility scrutiny

### 5. Enterprise roadmap
`Use dilbert-council standard review this roadmap: "Add SSO, audit logs, and role-based access control before moving upmarket."`

Expected signal:
- More nuanced scorecard
- Alice and Dilbert should disagree productively on sequencing versus completeness

### 6. Agency or services business
`Use dilbert-council standard review this business: "Done-for-you AI automation setup for small law firms."`

Expected signal:
- Dogbert flags liability and trust
- Wally flags support burden and process drift
- Next-step plan narrows scope aggressively

### 7. Personal productivity tool
`Use dilbert-council quick-roast this idea: "A private journaling app that turns your day into action items."`

Expected signal:
- Short, low-stakes output
- No over-engineered claim ledger

### 8. PR-sensitive launch
`Use dilbert-council deep-dive this launch plan: "Ship a browser agent that can log into customer bank accounts and summarize spending."`

Expected signal:
- High-stakes escalation
- Verdict should not be softened by launch excitement
- Cross-examination should expose any unrealistic optimism

### 9. Research synthesis critique
`Use dilbert-council standard review this research report: outputs/research-openai-codex-gpt55-images20-2026-04-29.html`

Expected signal:
- Separate official facts from market interpretation.
- Treat "Codex is becoming the agentic work surface" as an inference, not a fact.
- Include a fact / inference / unknown split.
- Include an availability matrix for Codex, GPT-5.5, Images 2.0, workspace agents, and AWS when claims depend on availability.
- Explicitly state that model benchmarks are not workflow proof.
- Add a falsifiable 7-day workflow test.
- Dogbert should attack narrative inflation.
- Dilbert should test whether the stack closes an actual work loop.
- Alice should force one owner, one benchmark workflow, and one fail threshold.

## Regression Notes
- Keep a small set of favorite prompts and compare runs over time.
- Watch for regressions in differentiation first. Repetition is usually the first sign the council is collapsing into style theater.
- Watch for overfitting to the renderer. Clean HTML is not proof of better thinking.
