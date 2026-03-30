#!/usr/bin/env -S uv --quiet run --active --script
# /// script
# requires-python = ">=3.11"
# ///
"""Render a Dilbert Council HTML report from the JSON sidecar."""

from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from typing import Any, TypedDict


class Meta(TypedDict, total=False):
    subject_title: str
    subject_slug: str
    topic: str
    mode: str
    generated_at: str
    file_ref: str
    traffic_light: str
    confidence: str
    maturity_level: str
    stakes_level: str
    directive: str
    footer_note: str
    report_title_line_1: str
    report_title_line_2: str


class ScorecardEntry(TypedDict, total=False):
    criterion: str
    weight: int
    score: int
    why: str


class ClaimLedgerEntry(TypedDict, total=False):
    id: str
    type: str
    confidence: str
    claim: str
    source_or_test: str
    why_it_matters: str


class CharacterMatrixEntry(TypedDict, total=False):
    character: str
    stance: str
    core_fear: str
    most_useful_recommendation: str


class RiskEntry(TypedDict, total=False):
    name: str
    probability: str
    impact: str
    mitigation: str


class CrossExamEntry(TypedDict, total=False):
    character: str
    target_character: str
    claim_id: str
    challenge: str
    falsifier: str
    verdict_delta: str


class SourceEntry(TypedDict, total=False):
    label: str
    url_or_path: str
    used_for: str


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Render a Dilbert Council HTML report from a JSON sidecar."
    )
    parser.add_argument(
        "input_json",
        type=Path,
        help="Path to a council JSON sidecar, typically <subject-slug>-dilbert-council-report.json",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Output HTML path. Defaults to <subject-slug>-dilbert-council-report.html.",
    )
    parser.add_argument(
        "--template",
        type=Path,
        help="Optional HTML template path. Defaults to the skill template.",
    )
    parser.add_argument(
        "--image-base",
        default=".codex/skills/dilbert-council/assets/images",
        help="Image base path used in the rendered HTML.",
    )
    return parser.parse_args()


def read_json(path: Path) -> dict[str, Any]:
    """Load and validate the JSON sidecar."""
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(data, dict):
        raise ValueError("Top-level JSON value must be an object.")
    return data


def slugify_subject(value: str) -> str:
    """Create a filesystem-safe slug for the council subject."""
    lowered = value.strip().lower()
    normalized = re.sub(r"[^a-z0-9]+", "-", lowered)
    normalized = re.sub(r"-{2,}", "-", normalized).strip("-")
    return normalized or "untitled-subject"


def escape(value: Any) -> str:
    """HTML-escape arbitrary values."""
    return html.escape(str(value), quote=True)


def ensure_list(value: Any) -> list[Any]:
    """Normalize a value into a list."""
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def render_list_items(items: list[Any]) -> str:
    """Render a list into <li> elements."""
    normalized = [escape(item) for item in items if str(item).strip()]
    if not normalized:
        return "<li>None noted.</li>"
    return "".join(f"<li>{item}</li>" for item in normalized)


def render_key_value_list(items: list[tuple[str, Any]]) -> str:
    """Render labeled items into <li> elements."""
    rows: list[str] = []
    for label, value in items:
        if value is None:
            continue
        if isinstance(value, list):
            joined = ", ".join(str(part) for part in value if str(part).strip())
            if not joined:
                continue
            rows.append(f"<li><strong>{escape(label)}:</strong> {escape(joined)}</li>")
            continue
        text = str(value).strip()
        if not text:
            continue
        rows.append(f"<li><strong>{escape(label)}:</strong> {escape(text)}</li>")
    return "".join(rows) if rows else "<li>Not provided.</li>"


def render_council_read(value: Any) -> str:
    """Render the short top-level council synthesis."""
    if value is None:
        return "No council read supplied."
    if isinstance(value, list):
        parts = [str(item).strip() for item in value if str(item).strip()]
        return escape(" ".join(parts)) if parts else "No council read supplied."
    text = str(value).strip()
    return escape(text) if text else "No council read supplied."


def split_in_half(items: list[Any]) -> tuple[list[Any], list[Any]]:
    """Split a list into two balanced halves."""
    midpoint = (len(items) + 1) // 2
    return items[:midpoint], items[midpoint:]


def traffic_light_class(value: str) -> str:
    """Map a traffic-light label to a CSS class."""
    key = value.strip().lower()
    return {
        "green": "rating-green",
        "yellow": "rating-yellow",
        "red": "rating-red",
    }.get(key, "")


def render_scorecard(entries: list[ScorecardEntry]) -> str:
    """Render scorecard rows."""
    if not entries:
        return (
            "<tr><td colspan=\"4\">No scorecard supplied. Add weighted criteria in the JSON sidecar.</td></tr>"
        )
    rows: list[str] = []
    for entry in entries:
        rows.append(
            "<tr>"
            f"<td>{escape(entry.get('criterion', ''))}</td>"
            f"<td>{escape(entry.get('weight', ''))}</td>"
            f"<td>{escape(entry.get('score', ''))}</td>"
            f"<td>{escape(entry.get('why', ''))}</td>"
            "</tr>"
        )
    return "".join(rows)


def render_claim_ledger(entries: list[ClaimLedgerEntry]) -> str:
    """Render claim-ledger rows."""
    if not entries:
        return (
            "<tr><td colspan=\"6\">No claim ledger supplied. Add shared claims before exporting.</td></tr>"
        )
    rows: list[str] = []
    for entry in entries:
        rows.append(
            "<tr>"
            f"<td>{escape(entry.get('id', ''))}</td>"
            f"<td>{escape(entry.get('type', ''))}</td>"
            f"<td>{escape(entry.get('confidence', ''))}</td>"
            f"<td>{escape(entry.get('claim', ''))}</td>"
            f"<td>{escape(entry.get('source_or_test', ''))}</td>"
            f"<td>{escape(entry.get('why_it_matters', ''))}</td>"
            "</tr>"
        )
    return "".join(rows)


def render_character_matrix(entries: list[CharacterMatrixEntry], image_base: str) -> str:
    """Render the character contrast matrix."""
    image_names = {
        "dilbert": "Dilbert.png",
        "alice": "Alice.png",
        "wally": "Wally.png",
        "dogbert": "Dogbert.png",
        "phb": "PHB.png",
    }
    rows: list[str] = []
    for entry in entries:
        character = str(entry.get("character", "")).strip()
        key = character.lower()
        image_name = image_names.get(key, "")
        class_name = traffic_light_class(str(entry.get("stance", "")))
        stance = escape(entry.get("stance", ""))
        stance_html = (
            f"<strong class=\"{class_name}\">{stance}</strong>" if class_name else stance
        )
        image_html = (
            f"<img class=\"matrix-avatar\" src=\"{escape(image_base)}/{escape(image_name)}\" alt=\"{escape(character)}\"><span class=\"sr-only\">{escape(character)}</span>"
            if image_name
            else escape(character)
        )
        rows.append(
            "<tr>"
            f"<td>{image_html}</td>"
            f"<td>{stance_html}</td>"
            f"<td>{escape(entry.get('core_fear', ''))}</td>"
            f"<td>{escape(entry.get('most_useful_recommendation', ''))}</td>"
            "</tr>"
        )
    return "".join(rows) if rows else "<tr><td colspan=\"4\">No matrix data supplied.</td></tr>"


def render_risks(entries: list[RiskEntry]) -> str:
    """Render risk cards."""
    if not entries:
        return (
            "<article class=\"risk mono\"><strong>No risk list supplied</strong>"
            "<div>Add ranked risks to the JSON sidecar.</div></article>"
        )
    blocks: list[str] = []
    for index, entry in enumerate(entries, start=1):
        blocks.append(
            "<article class=\"risk mono\">"
            f"<strong>{escape(index)}) {escape(entry.get('name', ''))}</strong>"
            f"<div>Probability: {escape(entry.get('probability', ''))} | "
            f"Impact: {escape(entry.get('impact', ''))} | "
            f"Mitigation: {escape(entry.get('mitigation', ''))}</div>"
            "</article>"
        )
    return "".join(blocks)


def render_next_7_days(value: Any) -> str:
    """Render the 7-day plan."""
    if isinstance(value, dict):
        items = [
            ("Owner", value.get("owner")),
            ("Scope", value.get("scope")),
            ("Success threshold", value.get("success_threshold")),
            ("Fail threshold", value.get("fail_threshold")),
        ]
        return render_key_value_list(items)
    return render_list_items(ensure_list(value))


def render_decision_gates(value: Any) -> tuple[str, str]:
    """Render decision gates into two columns."""
    if not isinstance(value, dict):
        items = ensure_list(value)
        left, right = split_in_half(items)
        return render_list_items(left), render_list_items(right)
    left = [
        f"Go if: {item}" for item in ensure_list(value.get("go_if"))
    ]
    right = [
        f"Hold if: {item}" for item in ensure_list(value.get("hold_if"))
    ] + [f"Kill if: {item}" for item in ensure_list(value.get("kill_if"))]
    return render_list_items(left), render_list_items(right)


def render_memo_cards(memos: dict[str, Any], image_base: str) -> str:
    """Render memo cards in council order."""
    order = [
        ("dilbert", "Dilbert"),
        ("alice", "Alice"),
        ("wally", "Wally"),
        ("dogbert", "Dogbert"),
        ("phb", "PHB"),
    ]
    image_names = {
        "dilbert": "Dilbert.png",
        "alice": "Alice.png",
        "wally": "Wally.png",
        "dogbert": "Dogbert.png",
        "phb": "PHB.png",
    }
    cards: list[str] = []
    for key, label in order:
        markdown = str(memos.get(key, "")).strip() or f"## {label}\n- Memo missing."
        details_tag = "<details open>" if key == "dilbert" else "<details>"
        cards.append(
            "<article class=\"memo-card\">"
            f"<img class=\"memo-avatar\" src=\"{escape(image_base)}/{escape(image_names[key])}\" alt=\"{escape(label)}\">"
            f"{details_tag}"
        )
        cards.append(
            f"<summary>{escape(label)} - Primary Memo</summary>"
            f"<pre class=\"memo-text\">{escape(markdown)}</pre>"
            "</details>"
            "</article>"
        )
    return "".join(cards)


def render_cross_exam(entries: list[CrossExamEntry], image_base: str) -> str:
    """Render cross-examination cards."""
    image_names = {
        "dilbert": "Dilbert.png",
        "alice": "Alice.png",
        "wally": "Wally.png",
        "dogbert": "Dogbert.png",
        "phb": "PHB.png",
    }
    if not entries:
        return (
            "<div class=\"memo-card\">"
            f"<img class=\"memo-avatar\" src=\"{escape(image_base)}/Dilbert.png\" alt=\"Cross-examination\">"
            "<pre class=\"memo-text\">No directed cross-examination supplied.</pre>"
            "</div>"
        )
    blocks: list[str] = []
    for entry in entries:
        character = str(entry.get("character", "")).strip()
        image_name = image_names.get(character.lower(), "Dilbert.png")
        lines = [
            f"- Claim attacked: {entry.get('claim_id', '')} against {entry.get('target_character', '')}",
            f"- Challenge: {entry.get('challenge', '')}",
            f"- Falsifier or rescue test: {entry.get('falsifier', '')}",
            f"- Verdict delta: {entry.get('verdict_delta', '')}",
        ]
        blocks.append(
            "<div class=\"memo-card\">"
            f"<img class=\"memo-avatar\" src=\"{escape(image_base)}/{escape(image_name)}\" alt=\"{escape(character)} cross-exam\">"
            f"<pre class=\"memo-text\">{escape(chr(10).join(lines))}</pre>"
            "</div>"
        )
    return "".join(blocks)


def render_sources(entries: list[SourceEntry]) -> str:
    """Render the sources list."""
    if not entries:
        return "<li>No external sources were used.</li>"
    rows: list[str] = []
    for entry in entries:
        label = escape(entry.get("label", "Source"))
        url_or_path = escape(entry.get("url_or_path", ""))
        used_for = escape(entry.get("used_for", ""))
        if used_for:
            rows.append(f"<li><code>{label}</code> - {url_or_path} - {used_for}</li>")
        else:
            rows.append(f"<li><code>{label}</code> - {url_or_path}</li>")
    return "".join(rows)


def replace_placeholders(template: str, replacements: dict[str, str]) -> str:
    """Replace template placeholders."""
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def render_html_report(data: dict[str, Any], template: str, image_base: str) -> str:
    """Render the final HTML string."""
    meta: Meta = data.get("meta", {})
    idea_snapshot: dict[str, Any] = data.get("idea_snapshot", {})
    evidence_snapshot: dict[str, Any] = data.get("evidence_snapshot", {})
    overall_verdict: dict[str, Any] = data.get("overall_verdict", {})

    left_snapshot = [
        ("Problem", idea_snapshot.get("problem")),
        ("Proposal", idea_snapshot.get("proposal")),
        ("Beneficiary", idea_snapshot.get("beneficiary")),
        ("Constraints", idea_snapshot.get("constraints")),
        ("Success signal", idea_snapshot.get("success_signal")),
    ]
    right_snapshot = [
        ("Decision requested", idea_snapshot.get("decision_requested")),
        ("Reversibility", idea_snapshot.get("reversibility")),
        ("Time horizon", idea_snapshot.get("time_horizon")),
        ("Maturity", idea_snapshot.get("maturity_level", meta.get("maturity_level"))),
        ("Stakes", idea_snapshot.get("stakes_level", meta.get("stakes_level"))),
    ]

    consensus_left, consensus_right = split_in_half(ensure_list(data.get("consensus")))

    traffic_light = str(
        overall_verdict.get("traffic_light", meta.get("traffic_light", "Yellow"))
    )
    confidence = str(overall_verdict.get("confidence", meta.get("confidence", "Medium")))
    decision_gates_left, decision_gates_right = render_decision_gates(
        data.get("decision_gates", {})
    )

    meta_html = "<br>\n          ".join(
        [
            f"DATE: {escape(meta.get('generated_at', ''))}",
            f"TOPIC: {escape(meta.get('topic', 'Dilbert Council Report'))}",
            f"MODE: {escape(meta.get('mode', 'standard'))}",
            f"STAKES: {escape(meta.get('stakes_level', idea_snapshot.get('stakes_level', '')))}",
        ]
    )

    replacements = {
        "DOC_TITLE": escape(meta.get("topic", "Dilbert Council Report")),
        "FILE_REF": escape(meta.get("file_ref", "DILBERT-COUNCIL")),
        "TRAFFIC_LIGHT_TEXT": escape(traffic_light),
        "TRAFFIC_LIGHT_CLASS": traffic_light_class(traffic_light),
        "REPORT_TITLE_LINE_1": escape(meta.get("report_title_line_1", "Council")),
        "REPORT_TITLE_LINE_2": escape(meta.get("report_title_line_2", "Report")),
        "META_HTML": meta_html,
        "CONFIDENCE": escape(confidence),
        "MATURITY_LEVEL": escape(
            meta.get("maturity_level", idea_snapshot.get("maturity_level", ""))
        ),
        "STAKES_LEVEL": escape(
            meta.get("stakes_level", idea_snapshot.get("stakes_level", ""))
        ),
        "DIRECTIVE": escape(meta.get("directive", "Decision-focused critique")),
        "IMAGE_BASE": escape(image_base),
        "IDEA_SNAPSHOT_LEFT_HTML": render_key_value_list(left_snapshot),
        "IDEA_SNAPSHOT_RIGHT_HTML": render_key_value_list(right_snapshot),
        "COUNCIL_READ_HTML": render_council_read(data.get("council_read")),
        "MEMORABLE_LINES_HTML": render_list_items(ensure_list(data.get("memorable_lines"))),
        "SCORECARD_ROWS_HTML": render_scorecard(ensure_list(data.get("scorecard"))),
        "EVIDENCE_FACTS_HTML": render_list_items(
            ensure_list(evidence_snapshot.get("facts"))
        ),
        "EVIDENCE_UNCERTAINTIES_HTML": render_list_items(
            ensure_list(evidence_snapshot.get("uncertainties"))
        ),
        "CLAIM_LEDGER_ROWS_HTML": render_claim_ledger(
            ensure_list(data.get("claim_ledger"))
        ),
        "OVERALL_VERDICT_HTML": render_list_items(
            ensure_list(overall_verdict.get("summary"))
        ),
        "MATRIX_ROWS_HTML": render_character_matrix(
            ensure_list(data.get("character_matrix")), image_base
        ),
        "CONSENSUS_LEFT_HTML": render_list_items(consensus_left),
        "CONSENSUS_RIGHT_HTML": render_list_items(consensus_right),
        "DISAGREEMENTS_HTML": render_list_items(ensure_list(data.get("disagreements"))),
        "TOP_RISKS_HTML": render_risks(ensure_list(data.get("top_risks"))),
        "WHAT_NOT_TO_DO_HTML": render_list_items(ensure_list(data.get("what_not_to_do"))),
        "NEXT_7_DAYS_HTML": render_next_7_days(data.get("next_7_days")),
        "NEXT_30_DAYS_HTML": render_list_items(ensure_list(data.get("next_30_days"))),
        "DECISION_GATES_LEFT_HTML": decision_gates_left,
        "DECISION_GATES_RIGHT_HTML": decision_gates_right,
        "QUESTIONS_HTML": render_list_items(ensure_list(data.get("questions_for_user"))),
        "CROSS_EXAM_HTML": render_cross_exam(
            ensure_list(data.get("cross_examination")), image_base
        ),
        "MEMO_CARDS_HTML": render_memo_cards(
            data.get("memos", {}), image_base
        ),
        "SOURCES_HTML": render_sources(ensure_list(data.get("sources"))),
        "FOOTER_NOTE": escape(
            meta.get(
                "footer_note",
                "CONFIDENTIAL - COUNCIL WORKING PAPER - DO NOT DISTRIBUTE WITHOUT CONTEXT",
            )
        ),
    }

    return replace_placeholders(template, replacements)


def default_template_path() -> Path:
    """Return the default template path."""
    return (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "templates"
        / "dilbert-council-report-template.html"
    )


def subject_slug_for_data(data: dict[str, Any]) -> str:
    """Resolve the council subject slug from metadata."""
    meta: Meta = data.get("meta", {})
    raw_slug = str(meta.get("subject_slug", "")).strip()
    if raw_slug:
        return slugify_subject(raw_slug)

    subject_title = str(meta.get("subject_title", "")).strip()
    if subject_title:
        return slugify_subject(subject_title)

    topic = str(meta.get("topic", "")).strip()
    if topic:
        return slugify_subject(topic)

    return "untitled-subject"


def default_output_path(input_json: Path, data: dict[str, Any]) -> Path:
    """Build the default HTML path using the shared subject prefix."""
    subject_slug = subject_slug_for_data(data)
    return input_json.with_name(f"{subject_slug}-dilbert-council-report.html")


def main() -> int:
    """Run the renderer."""
    args = parse_args()
    data = read_json(args.input_json)
    template_path = args.template or default_template_path()
    output_path = args.output or default_output_path(args.input_json, data)
    template = template_path.read_text(encoding="utf-8")
    rendered = render_html_report(data, template, args.image_base)
    output_path.write_text(rendered, encoding="utf-8")
    print(f"Rendered {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
