---
name: dilbert-council
description: Use when the user wants a ruthless, funny, high-signal critique of an idea, proposal, roadmap, or execution plan. Works for rough ideas and detailed plans. Runs five Dilbert-character agents (dilbert, alice, wally, dogbert, phb), optionally adds a shared web-research evidence packet when external facts matter, and returns a contrast-rich Council Report with actionable next steps.
---

# Dilbert Council Skill

## Objective
Deliver output that is both hilarious and decision-useful.

Target qualities:
- Strong character contrast.
- Concrete recommendations.
- Clear decision framing.
- Fast next-step plan.

## Run Modes
Choose a mode before running the council.

- `quick-roast`: For simple ideas. No rebuttal round. Keep answers short.
- `standard`: Default for most requests. Full council + synthesis.
- `deep-dive`: For detailed plans. Add rebuttal round and richer risk analysis.

## Step 1: Normalize the user input
Create an `Idea Brief` before spawning agents.

Include:
- Problem: What pain is being solved.
- Proposal: What the user wants to build/do.
- Beneficiary: Who benefits or buys.
- Constraints: Budget, timeline, team, tech, risk tolerance.
- Success signal: How the user will know it worked.
- Maturity level: `seed`, `brief`, or `plan`.

Use this rubric:
- `seed`: 1 to 3 rough sentences or bullets.
- `brief`: 4 to 12 concrete bullets.
- `plan`: Detailed multi-part plan with assumptions/dependencies.

## Step 2: Decide if web research is needed
Prefer a single shared research pass by the orchestrator, not five independent searches.

Use web research when external facts materially affect the verdict:
- Market size, competitors, pricing, regulation, legal risk, security claims.
- Tool/library capabilities or limits.
- Time-sensitive claims.

Skip web research when the task is mostly internal judgment:
- Team/process design.
- Personal productivity ideas.
- Fictional or purely conceptual brainstorming.
- User already supplied sufficient facts.

If research is needed, build an `Evidence Packet` first:
1. Gather 4 to 8 high-quality sources.
2. Extract only decision-relevant facts.
3. Label each fact with date and source.
4. List open uncertainties explicitly.

Pass the same `Evidence Packet` to every agent to keep the debate grounded and consistent.

## Step 3: Spawn the five agents in parallel
Spawn exactly:
- `dilbert`
- `alice`
- `wally`
- `dogbert`
- `phb`

Give each agent:
- `Idea Brief`
- User constraints
- Optional `Evidence Packet`
- This shared instruction:

"""
Stay in character. Be funny but useful. Avoid random jokes and filler.
Tie every major criticism to a concrete action or test.
Separate assumptions from facts. If Evidence Packet exists, use it.
Follow your output template exactly.
"""

Length guidance by maturity:
- `seed`: 180 to 280 words per agent.
- `brief`: 250 to 380 words per agent.
- `plan`: 320 to 500 words per agent.

## Step 4: Optional rebuttal pass (deep-dive mode)
Only for `plan` maturity or when requested.

Ask each agent for a short addendum:
- Best point from another agent (1 bullet).
- Biggest disagreement with another agent (1 bullet).
- What this changes in their verdict (1 sentence).

Use this to increase contrast quality and reduce fake consensus.

## Step 5: Produce the Council Report
Use this exact structure.

# Council Report
## Idea Snapshot
- Problem
- Proposal
- Constraints
- Success signal
- Maturity level

## Overall Verdict
- Traffic light: Green / Yellow / Red
- Confidence: Low / Medium / High
- Why: 2 to 4 bullets

## Character Contrast Matrix
Use a compact table:
- Character
- Stance
- Core fear
- Most useful recommendation

## Consensus (What almost everyone agrees on)
Bullets only.

## Productive Disagreements (Where contrast is valuable)
Bullets only.

## Top Risks (ranked)
For each risk: probability, impact, and mitigation.

## What Not To Do
Call out tempting but damaging moves.

## 7-Day Minimum Viable Next Step
Concrete experiment with owner, scope, and success/fail threshold.

## 30-Day De-Risk Plan
Include only for `plan` maturity.

## Decision Gates
- Go if:
- Hold if:
- Kill if:

## Questions for the User
Max 7. Only high-leverage questions.

## Appendix: Individual Memos
Paste each agent output verbatim under labels.

## Sources
Include only when web research was used.

## Quality Bar
Meet all checks before finalizing:
- Distinct voices are obvious in one paragraph each.
- Humor supports the point instead of replacing analysis.
- At least one practical recommendation from each character survives into synthesis.
- Final recommendation is executable in 7 days.
- No section is generic or filler.

## Anti-Patterns to avoid
- Running five separate web searches per agent for the same topic.
- Producing consensus-only output that hides real disagreements.
- Making jokes without decision value.
- Giving risks without mitigation.
- Ending without a concrete next step.