# Dilbert Council for Codex

Codex-only multi-agent setup for ruthless, funny, high-signal idea and plan reviews using five Dilbert characters:

- `dilbert`
- `alice`
- `wally`
- `dogbert`
- `phb`

This repository is designed to be cloned and used directly with Codex. It ships the full local `.codex` configuration (agents + skill) so no extra setup is needed beyond running Codex in this folder.

## Tribute Disclaimer

This project is a fan tribute to the legendary Scott Adams and the Dilbert comic universe and characters. It is an unofficial, community-built configuration for Codex and is not affiliated with or endorsed by Scott Adams, Dilbert, or associated rights holders.

## Requirements

- Codex `>= 0.104` (multi-agent capability required).
- Check your version with `codex --version`.
- If your version is lower, update Codex first, then run this repo.

## What You Get

- A reusable skill: `.codex/skills/dilbert-council/SKILL.md`
- Five character agent configs: `.codex/agents/*.toml`
- Structured output workflow tuned for humor with clear character contrast.
- Structured output workflow tuned for practical decision support.
- Structured output workflow tuned for both simple ideas (`seed`) and detailed plans (`plan`).

## Quick Start

1. Clone this repo.
2. Open a terminal in the repo root.
3. Launch Codex in this directory (`codex`).
4. Ask Codex to run the skill.

Example prompts:

- `Use dilbert-council quick-roast this idea: "AI meal planner for families".`
- `Use dilbert-council deep-dive this plan and do web research first.`
- `Run the council on this proposal and give me go/hold/kill gates.`

## First 5 Minutes

Use this exact smoke test after cloning:

1. Start Codex in this repo: `codex`
2. Paste this prompt:
`Use dilbert-council quick-roast this idea: "Build an AI-powered personal kanban app with a monthly subscription for non-corporate users."`
3. Confirm output includes:
- all five character memos (`Dilbert`, `Alice`, `Wally`, `Dogbert`, `PHB`)
- one consolidated `Council Report`
- an overall verdict and a concrete 7-day next step
4. Run a deep-dive test prompt:
`Use dilbert-council deep-dive this plan and use web research first. Then include go/hold/kill gates and sources.`

## Repository Structure

- `.codex/config.toml`: Local Codex config entry point.
- `.codex/skills/dilbert-council/SKILL.md`: Skill workflow and report format.
- `.codex/agents/dilbert.toml`: Engineering realism and hidden complexity.
- `.codex/agents/alice.toml`: Execution rigor and scope discipline.
- `.codex/agents/wally.toml`: Incentive/process failure detection.
- `.codex/agents/dogbert.toml`: Adversarial strategy, exploitability, PR/legal risk.
- `.codex/agents/phb.toml`: Exec theater failure modes and metric abuse.

## Run Modes

Defined in the skill:

- `quick-roast`: Fast, high-signal critique for rough ideas.
- `standard`: Default balanced run.
- `deep-dive`: Full analysis for detailed plans (includes rebuttal pass).

## Web Research Behavior

The skill supports optional research-first runs.

- Use web research when external facts materially affect decisions (market demand, competitors, pricing, regulation, security incidents, time-sensitive claims).
- Skip web research for mostly internal judgment calls (org design, team process, conceptual brainstorming).

When enabled, research should be centralized into one shared **Evidence Packet** before spawning agents. Do not run redundant per-agent web searches by default.

## Output Shape

The council report is structured to maximize usefulness:

- idea snapshot
- overall verdict + confidence
- character contrast matrix
- consensus and productive disagreements
- ranked risks with mitigations
- 7-day next step
- 30-day de-risk plan (for deep-dive)
- decision gates (`go` / `hold` / `kill`)
- appendix with full individual memos

## HTML Report Export (Optional)

After generating the council report, the skill can optionally create a styled local HTML report.

- Output file (current working directory): `dilbert_council_report.html`
- Template source: `.codex/skills/dilbert-council/assets/templates/dilbert-council-report-template.html`
- Image assets used by the template:
  - `.codex/skills/dilbert-council/assets/images/dilbert-logo-small.png`
  - `.codex/skills/dilbert-council/assets/images/Dilbert.png`
  - `.codex/skills/dilbert-council/assets/images/Alice.png`
  - `.codex/skills/dilbert-council/assets/images/Wally.png`
  - `.codex/skills/dilbert-council/assets/images/Dogbert.png`
  - `.codex/skills/dilbert-council/assets/images/PHB.png`

The export preserves the report look-and-feel and readability details:

- Manila-folder visual style and report layout
- Character image sizing (appendix/rebuttal avatars at 50%)
- Character image icons in the contrast matrix
- Markdown-to-HTML rendering for appendix memos/rebuttals (`#` headings, `**bold**`, bullets)
- Color-coded risk labels (`Green`, `Yellow`, `Red`) via CSS classes

Preview reference: ![council-report-snip.png](council-report-snip.png)

## Customization

Adjust character behavior in:

- `.codex/agents/alice.toml`
- `.codex/agents/dilbert.toml`
- `.codex/agents/wally.toml`
- `.codex/agents/dogbert.toml`
- `.codex/agents/phb.toml`

Adjust orchestration/reporting in:

- `.codex/skills/dilbert-council/SKILL.md`

## Usage Notes

- Keep prompts explicit about mode (`quick-roast`, `standard`, or `deep-dive`).
- For deep-dive, provide constraints and desired success criteria.
- If you want source-backed conclusions, explicitly ask for web research.

## Codex Scope

This repository is intended for Codex local `.codex` workflows. It is not packaged as a general-purpose library or framework.
