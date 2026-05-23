from pathlib import Path

from src.storage import LocalStore


def test_storage_roundtrip(tmp_path: Path):
    store = LocalStore(data_dir=tmp_path / "data")

    impulse = {
        "what_appeared": "fog",
        "concrete_movement_action": "stand up",
        "next_tiny_build_step": "open notebook",
    }
    store.add_impulse(impulse)

    research = {
        "source_title": "Note",
        "one_sentence_insight": "Clarity follows action.",
        "practice_translation": "Start with one physical motion.",
        "open_question": "What cue repeats best?",
    }
    store.add_research_note(research)

    review = {
        "what_pulled_me_in": "short loops",
        "what_stayed_dead": "long plans",
        "what_should_repeat_next_week": "daily grip",
        "what_should_be_removed": "extra tabs",
    }
    store.add_weekly_review(review)

    assert impulse in store.list_items("impulses")
    assert research in store.list_items("research_notes")
    assert review in store.list_items("weekly_reviews")


def test_seed_practices_created(tmp_path: Path):
    store = LocalStore(data_dir=tmp_path / "data")
    practices = store.list_items("practices")
    assert len(practices) >= 6


def test_no_cloud_api_assumptions_in_storage_module():
    text = open("src/storage.py", encoding="utf-8").read().lower()
    forbidden = ["openai", "http://", "https://", "requests", "sqlalchemy", "boto3"]
    for token in forbidden:
        assert token not in text
