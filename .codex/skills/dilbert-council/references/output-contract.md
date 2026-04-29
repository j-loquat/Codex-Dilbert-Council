# Dilbert Council Output Contract

Use this contract when a run needs machine-readable output or HTML export.

The council should always build this structure internally before writing prose. If the user asks for files, write them with a shared subject prefix and render the HTML from the JSON sidecar.

Use a shared subject prefix for exported artifacts:

- `<subject-slug>-dilbert-council-report.json`
- `<subject-slug>-dilbert-council-report.html`

## Required Top-Level Keys
- `meta`
- `idea_snapshot`
- `council_read`
- `memorable_lines`
- `scorecard`
- `evidence_snapshot`
- `claim_ledger`
- `fact_inference_unknown`
- `availability_matrix`
- `source_hierarchy`
- `overall_verdict`
- `character_matrix`
- `consensus`
- `disagreements`
- `top_risks`
- `what_not_to_do`
- `next_7_days`
- `test_plan`
- `decision_gates`
- `verdict_sensitivity`
- `questions_for_user`
- `memos`
- `cross_examination`
- `sources`

## Recommended Shape

```json
{
  "meta": {
    "subject_title": "ZeroClaw remote install service",
    "subject_slug": "zero-claw-remote-install-service",
    "topic": "ZeroClaw remote install service",
    "mode": "deep-dive",
    "generated_at": "2026-03-27T10:05:00-04:00",
    "file_ref": "ZERO-CLAW-REMOTE-INSTALL-SERVICE-DILBERT-COUNCIL-2026-03-27",
    "traffic_light": "Yellow",
    "confidence": "Medium-High",
    "maturity_level": "plan",
    "stakes_level": "high",
    "directive": "Concierge MVP only",
    "model_routing": {
      "visible_agents": "gpt-5.5 high reasoning via persona-injected default agents",
      "scribe": "gpt-5.5 high reasoning",
      "arbiter": "gpt-5.5 high reasoning",
      "reason": "Named runtime roles were pinned to older model families"
    },
    "footer_note": "CONFIDENTIAL - COUNCIL WORKING PAPER - DO NOT DISTRIBUTE WITHOUT CONTEXT"
  },
  "idea_snapshot": {
    "problem": "Setup complexity and trust risk block adoption.",
    "proposal": "Build a remote installation service.",
    "beneficiary": "Non-technical always-on AI users.",
    "constraints": [
      "1-week MVP",
      "High trust sensitivity"
    ],
    "success_signal": ">=80% first-pass installs",
    "decision_requested": "Refine and test",
    "reversibility": "Medium",
    "time_horizon": "7 days",
    "maturity_level": "plan",
    "stakes_level": "high"
  },
  "council_read": [
    "This is a trust business dressed up as an install service.",
    "The plan can work, but only if you stop pretending buttons are the same thing as proof."
  ],
  "memorable_lines": [
    "Dilbert: Nothing builds consumer confidence like asking strangers for SSH and calling it onboarding.",
    "Alice: You are not selling an installer; you are selling trust on a deadline."
  ],
  "scorecard": [
    {
      "criterion": "Demand",
      "weight": 4,
      "score": 3,
      "why": "User pain appears real, but demand concentration is thin."
    }
  ],
  "evidence_snapshot": {
    "facts": [
      "Security concerns dominate category discussion."
    ],
    "uncertainties": [
      "Upstream maintainability is still unclear."
    ]
  },
  "claim_ledger": [
    {
      "id": "CL-01",
      "type": "fact",
      "kind": "fact",
      "confidence": "0.90 high",
      "claim": "Trust is the core adoption blocker.",
      "evidence_refs": [
        "Evidence Packet source 2"
      ],
      "counterevidence_refs": [],
      "owner": "Dogbert",
      "decision_impact": "If false, the MVP can prioritize install speed over trust artifacts.",
      "expires_or_stale_when": "After the first 20 pilot installs or any category trust incident.",
      "test_needed": "Interview 10 target users and observe trust objections during install handoff.",
      "source_or_test": "Evidence Packet source 2, March 2026",
      "why_it_matters": "This changes MVP sequencing."
    }
  ],
  "fact_inference_unknown": {
    "facts": [
      "The official release timeline is source-backed."
    ],
    "inferences": [
      "The product cluster may indicate a broader strategy."
    ],
    "unknowns": [
      "Whether the product cluster improves the user's real workflow."
    ]
  },
  "availability_matrix": [
    {
      "feature": "Computer use in Codex",
      "plan_or_account": "ChatGPT signed-in Codex desktop users",
      "platform": "macOS initially",
      "region": "EU and UK rollout soon",
      "status": "Rolling out",
      "source": "OpenAI Codex product post",
      "confidence": "0.85 high",
      "decision_implication": "Do not assume this feature exists in every user's environment."
    }
  ],
  "source_hierarchy": [
    {
      "tier": "Official / primary",
      "supports": "Dates, product facts, pricing, availability, policy, and model-capability claims",
      "examples": [
        "OpenAI product posts",
        "OpenAI API docs"
      ],
      "limits": "Does not prove user adoption or workflow improvement unless it reports those directly."
    }
  ],
  "overall_verdict": {
    "traffic_light": "Yellow",
    "confidence": "Medium-High",
    "summary": [
      "The opportunity is real.",
      "The current scope is too broad for a safe week-1 launch."
    ]
  },
  "character_matrix": [
    {
      "character": "Dilbert",
      "stance": "Yellow",
      "core_fear": "Shipping before reliability gates",
      "most_useful_recommendation": "Cut scope and prove rollback first."
    }
  ],
  "consensus": [
    "No public launch in week 1."
  ],
  "disagreements": [
    "How much UX belongs in the first week."
  ],
  "top_risks": [
    {
      "name": "Trust boundary failure",
      "probability": "High",
      "impact": "Critical",
      "mitigation": "SSH keys only, no stored secrets, immutable logs."
    }
  ],
  "what_not_to_do": [
    "Do not market security claims without evidence."
  ],
  "next_7_days": {
    "owner": "Founder / Engineering lead",
    "scope": "Private concierge pilot on a narrow support matrix.",
    "success_threshold": "15/20 installs pass first attempt.",
    "fail_threshold": "Any high-severity secret flaw or rollback failure."
  },
  "test_plan": {
    "benchmark_tasks": [
      "One representative workflow against current baseline"
    ],
    "baseline": "Current manual or existing-tool workflow",
    "metrics": [
      "wall-clock time",
      "manual rescues",
      "cleanup time",
      "final quality",
      "cost or limits encountered"
    ],
    "pass_threshold": ">=25% median cycle-time reduction with equal or better quality",
    "fail_threshold": "No measurable gain or cleanup burden erases savings"
  },
  "next_30_days": [
    "Expand matrix only after trust gates pass."
  ],
  "decision_gates": {
    "go_if": [
      "Week-1 thresholds pass with security artifacts."
    ],
    "hold_if": [
      "Installs work but rollback or trust process is incomplete."
    ],
    "kill_if": [
      "Trust model requires major re-architecture."
    ]
  },
  "verdict_sensitivity": [
    "Greener if 15/20 pilot installs pass with no trust or rollback failures.",
    "Redder if users refuse the required access model even with clear security artifacts.",
    "Next unknown to resolve: whether trust objections appear before or after price discussion."
  ],
  "questions_for_user": [
    "Who owns incident response in week 1?"
  ],
  "memos": {
    "dilbert": "## Dilbert\n- TL;DR ...",
    "alice": "## Alice\n- TL;DR ...",
    "wally": "## Wally\n- TL;DR ...",
    "dogbert": "## Dogbert\n- TL;DR ...",
    "phb": "## PHB\n- TL;DR ..."
  },
  "cross_examination": [
    {
      "character": "Alice",
      "target_character": "PHB",
      "claim_id": "CL-06",
      "challenge": "Soft-launch pressure ignores trust gates.",
      "falsifier": "Show security artifacts and passing rollback drills.",
      "verdict_delta": "Yellow -> Red if gates slip."
    }
  ],
  "sources": [
    {
      "label": "OpenAI product post",
      "url_or_path": "https://example.com",
      "used_for": "Demand and timing context"
    }
  ]
}
```

## Field Notes

### `meta`
- Required for exports.
- `subject_title` should be a short human-readable title for the run.
- `subject_slug` should be the filesystem-safe prefix used for both exported files.
- `traffic_light` should be `Green`, `Yellow`, or `Red`.
- `confidence` can be `Low`, `Medium`, `High`, or a tighter string such as `Medium-High`.
- `model_routing` should record the model family or runtime route used for visible agents, scribe, and arbiter.

### `scorecard`
- Use 4 to 6 entries.
- `weight` should be `1` to `5`.
- `score` should be `1` to `5`.
- The final verdict should be consistent with the weighted pattern, not just the loudest memo.

### `council_read`
- Use 2 to 3 short sentences.
- Keep the tone lightly comic but accurate.
- This is the main place where the final synthesis keeps some council personality.
- If a sentence depends on a claim from the ledger, summarize the claim in prose instead of referencing only the ID.

### `memorable_lines`
- Use 0 to 3 short lines.
- Only keep lines that sharpen the recommendation or capture a failure mode.
- If a line is funny but empty, drop it.
- Do not fill this section with unexplained ledger shorthand.

### `claim_ledger`
- Keep it tight. Six to twelve claims is enough.
- Use `type` for the canonical claim type. `kind` is accepted as a backwards-compatible alias, but new artifacts should still write `type`.
- Every major synthesis point should cite one or more IDs from this list.
- When evidence is missing, use `type = "unknown"` or `type = "assumption"` and fill `source_or_test` with the resolving test.
- Prefer numeric confidence plus a short label, such as `0.75 medium`.
- Use `evidence_refs` and `counterevidence_refs` to show what supports or weakens the claim.
- Use `owner` to identify the persona responsible for defending the claim.
- Use `decision_impact` to say what changes if the claim is false.
- Use `expires_or_stale_when` for current facts, model capabilities, pricing, laws, competitors, and other time-sensitive claims.
- Use `test_needed` for the fastest practical resolving test.
- Outside the `claim_ledger` section itself, do not write bare IDs without a short plain-English summary.

### `fact_inference_unknown`
- Required for research-report critiques, market briefs, and AI product/tool reviews.
- Use three lists: `facts`, `inferences`, and `unknowns`.
- Strategic theses belong in `inferences` unless directly supported by a primary source.

### `availability_matrix`
- Required for AI products, tools, APIs, models, or platforms when availability affects the verdict.
- Each entry should include `feature`, `plan_or_account`, `platform`, `region`, `status`, `source`, `confidence`, and `decision_implication`.
- Use this to prevent preview, region-limited, platform-limited, or plan-gated features from being treated as universal.

### `source_hierarchy`
- Required for research-heavy runs.
- Classify sources by what they can support.
- Official and primary sources support product facts; third-party reporting supports market framing; social/search samples support sentiment examples; generic pages cannot prove enterprise readiness.

### `test_plan`
- Required when the verdict is Yellow because workflow value is unproven.
- Include benchmark tasks, baseline, metrics, pass threshold, and fail threshold.
- Use task-level tests for productivity or workflow claims; model benchmarks alone are not enough.

### Reader-facing prose rule
- In `overall_verdict`, `consensus`, `disagreements`, `top_risks`, `next_7_days`, and `decision_gates`, use plain-English claim summaries first.
- Optional format: `Trust is the main blocker (CL-01)`.
- Avoid format: `CL-01 and CL-04 imply a Yellow verdict`.

### `memos`
- Required keys: `dilbert`, `alice`, `wally`, `dogbert`, `phb`
- Preserve markdown. The renderer converts it to HTML later.

### `cross_examination`
- Include at least one entry for every deep-dive or high-stakes run.
- Each entry should attack a specific claim, not a vague vibe.

### `verdict_sensitivity`
- Required for deep-dive and high-stakes exports.
- Use 2 to 4 bullets.
- Say what would make the verdict greener, what would make it redder, and which unknown deserves the next test.

### `sources`
- Leave as an empty list when no research was used.
- Use absolute paths for local files when relevant.

## Renderer Expectations
`scripts/render_dilbert_council_report.py` expects this contract.

Invoke it with:

`uv run .codex/skills/dilbert-council/scripts/render_dilbert_council_report.py <subject-slug>-dilbert-council-report.json`

The renderer:
- tolerates missing optional keys such as `next_30_days`
- derives the default HTML filename from `meta.subject_slug`, `meta.subject_title`, or `meta.topic`
- renders markdown memo blocks into readable HTML
- keeps the council appendix and cross-examination blocks verbatim
- uses the template in `assets/templates/dilbert-council-report-template.html`
- supports `--strict` to fail export when required decision-quality fields are missing
- accepts `kind` as a claim-ledger alias for `type`, while rendering and validating it as the claim type
- makes http and https sources clickable in the generated HTML
- defaults image paths relative to the generated HTML file so reports can render from subfolders
