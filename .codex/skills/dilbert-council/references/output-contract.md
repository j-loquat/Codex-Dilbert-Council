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
- `overall_verdict`
- `character_matrix`
- `consensus`
- `disagreements`
- `top_risks`
- `what_not_to_do`
- `next_7_days`
- `decision_gates`
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
      "confidence": "high",
      "claim": "Trust is the core adoption blocker.",
      "source_or_test": "Evidence Packet source 2, March 2026",
      "why_it_matters": "This changes MVP sequencing."
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
- Every major synthesis point should cite one or more IDs from this list.
- When evidence is missing, use `type = "unknown"` or `type = "assumption"` and fill `source_or_test` with the resolving test.
- Outside the `claim_ledger` section itself, do not write bare IDs without a short plain-English summary.

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
