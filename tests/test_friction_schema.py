import pytest

from src import friction_schema as fs


def test_practice_schema_required_fields():
    payload = {"title": "x"}
    with pytest.raises(ValueError):
        fs.validate_practice(payload)


def test_impulse_required_fields():
    payload = {"what_appeared": "x"}
    with pytest.raises(ValueError):
        fs.validate_impulse(payload)


def test_research_required_fields():
    payload = {"source_title": "x"}
    with pytest.raises(ValueError):
        fs.validate_research_note(payload)


def test_weekly_review_required_fields():
    payload = {"what_pulled_me_in": "x"}
    with pytest.raises(ValueError):
        fs.validate_weekly_review(payload)


def test_practice_mode_must_be_allowed():
    valid = {
        "title": "t",
        "mode": "bauen",
        "adult_version": "a",
        "nina_version": "n",
        "shared_parent_child_version": "s",
        "duration": "1",
        "trigger": "t",
        "concrete_first_action": "c",
        "failure_mode": "f",
        "next_repetition_cue": "n",
    }
    fs.validate_practice(valid)
    invalid = dict(valid)
    invalid["mode"] = "unknown"
    with pytest.raises(ValueError):
        fs.validate_practice(invalid)


def test_no_cloud_api_assumptions_in_schema_module():
    text = open("src/friction_schema.py", encoding="utf-8").read().lower()
    forbidden = ["openai", "http://", "https://", "requests", "postgres", "mysql"]
    for token in forbidden:
        assert token not in text
