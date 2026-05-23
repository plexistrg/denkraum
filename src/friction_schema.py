"""Validation helpers for friction-first data structures."""

from __future__ import annotations

from typing import Iterable

PRACTICE_REQUIRED_FIELDS = [
    "title",
    "mode",
    "adult_version",
    "nina_version",
    "shared_parent_child_version",
    "duration",
    "trigger",
    "concrete_first_action",
    "failure_mode",
    "next_repetition_cue",
]

IMPULSE_REQUIRED_FIELDS = [
    "what_appeared",
    "concrete_movement_action",
    "next_tiny_build_step",
]

RESEARCH_REQUIRED_FIELDS = [
    "source_title",
    "one_sentence_insight",
    "practice_translation",
    "open_question",
]

WEEKLY_REVIEW_REQUIRED_FIELDS = [
    "what_pulled_me_in",
    "what_stayed_dead",
    "what_should_repeat_next_week",
    "what_should_be_removed",
]

ALLOWED_MODES = {"beruhigen", "vertiefen", "bauen"}


def missing_fields(payload: dict, required_fields: Iterable[str]) -> list[str]:
    return [field for field in required_fields if not str(payload.get(field, "")).strip()]


def validate_required_fields(payload: dict, required_fields: Iterable[str], label: str) -> None:
    missing = missing_fields(payload, required_fields)
    if missing:
        raise ValueError(f"{label} is missing required fields: {', '.join(missing)}")


def validate_practice(payload: dict) -> None:
    validate_required_fields(payload, PRACTICE_REQUIRED_FIELDS, "Practice")
    if payload["mode"] not in ALLOWED_MODES:
        raise ValueError(f"Practice mode must be one of {sorted(ALLOWED_MODES)}")


def validate_impulse(payload: dict) -> None:
    validate_required_fields(payload, IMPULSE_REQUIRED_FIELDS, "Impulse")


def validate_research_note(payload: dict) -> None:
    validate_required_fields(payload, RESEARCH_REQUIRED_FIELDS, "Research note")


def validate_weekly_review(payload: dict) -> None:
    validate_required_fields(payload, WEEKLY_REVIEW_REQUIRED_FIELDS, "Weekly review")
