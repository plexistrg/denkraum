"""Local JSON storage for Denkraum Studio."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.friction_schema import (
    validate_impulse,
    validate_practice,
    validate_research_note,
    validate_weekly_review,
)

DATA_DIR = Path("data")

FILES = {
    "practices": "practices.json",
    "impulses": "impulses.json",
    "research_notes": "research_notes.json",
    "weekly_reviews": "weekly_reviews.json",
}


SEED_PRACTICES = [
    {
        "title": "Slow reading with strong inner pronunciation",
        "mode": "vertiefen",
        "adult_version": "Read one short paragraph slowly and pronounce each word internally with full clarity.",
        "nina_version": "Read one sentence aloud very slowly and make each word sound big and clear.",
        "shared_parent_child_version": "Take turns reading one sentence slowly and exaggerate each important word.",
        "duration": "5 minutes",
        "trigger": "When thoughts drift and text becomes blurry.",
        "concrete_first_action": "Open one page and point to the first line with your finger.",
        "failure_mode": "Reading faster to finish instead of hearing each word.",
        "next_repetition_cue": "After lunch reading block.",
    },
    {
        "title": "Visual zooming into an object or image",
        "mode": "vertiefen",
        "adult_version": "Pick one object and mentally zoom from whole shape to tiny detail.",
        "nina_version": "Look at one toy and find three tiny parts you never noticed.",
        "shared_parent_child_version": "Choose one image and alternate calling out large and tiny details.",
        "duration": "4 minutes",
        "trigger": "When attention feels wide but unfocused.",
        "concrete_first_action": "Place one object in front of you and set a 4-minute timer.",
        "failure_mode": "Switching objects before reaching detail level.",
        "next_repetition_cue": "Before homework start.",
    },
    {
        "title": "Focus between letters / in-between spaces",
        "mode": "vertiefen",
        "adult_version": "Track white spaces between letters for one line, then read meaning.",
        "nina_version": "Find the tiny gaps between letters like little roads.",
        "shared_parent_child_version": "Both trace spaces between letters with a pencil without writing.",
        "duration": "3 minutes",
        "trigger": "When reading feels sticky.",
        "concrete_first_action": "Print or open one short sentence with large font.",
        "failure_mode": "Jumping to meaning too early.",
        "next_repetition_cue": "At the first sign of eye fatigue.",
    },
    {
        "title": "Hand-im-Gras grounding",
        "mode": "beruhigen",
        "adult_version": "Place your hand on grass or textured surface and narrate five sensations.",
        "nina_version": "Touch grass and name what your hand feels: cold, wet, soft, poky.",
        "shared_parent_child_version": "Both touch ground and trade one sensation at a time.",
        "duration": "2 minutes",
        "trigger": "When body tension rises.",
        "concrete_first_action": "Step outside or find a textured fabric and place palm flat.",
        "failure_mode": "Thinking about stress instead of sensing contact.",
        "next_repetition_cue": "Immediately after emotional spike.",
    },
    {
        "title": "Schwertgriff / next-grip practice",
        "mode": "bauen",
        "adult_version": "Name one concrete next grip and execute it before planning further.",
        "nina_version": "Pick one tiny move now: open notebook, draw first line, then stop.",
        "shared_parent_child_version": "Each person says one next grip and does it while the other watches.",
        "duration": "6 minutes",
        "trigger": "When ideas are many but movement is none.",
        "concrete_first_action": "Say aloud: 'My next grip is…' and start within 10 seconds.",
        "failure_mode": "Collecting options instead of choosing one move.",
        "next_repetition_cue": "Before any new project session.",
    },
    {
        "title": "4-in / 6-out breathing",
        "mode": "beruhigen",
        "adult_version": "Inhale for 4 counts, exhale for 6 counts, repeat 8 rounds.",
        "nina_version": "Smell the flower for 4, blow the candle for 6.",
        "shared_parent_child_version": "Breathe together and count out loud softly.",
        "duration": "3 minutes",
        "trigger": "When agitation blocks action.",
        "concrete_first_action": "Sit down and place one hand on chest and one on belly.",
        "failure_mode": "Breathing too fast to finish quickly.",
        "next_repetition_cue": "Right before difficult transitions.",
    },
]


class LocalStore:
    def __init__(self, data_dir: Path = DATA_DIR) -> None:
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_files()

    def _ensure_files(self) -> None:
        for key, filename in FILES.items():
            path = self.data_dir / filename
            if not path.exists():
                seed = SEED_PRACTICES if key == "practices" else []
                self._write_json(path, seed)

    def _write_json(self, path: Path, payload: list[dict[str, Any]]) -> None:
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def _read_json(self, path: Path) -> list[dict[str, Any]]:
        return json.loads(path.read_text(encoding="utf-8"))

    def list_items(self, bucket: str) -> list[dict[str, Any]]:
        return self._read_json(self.data_dir / FILES[bucket])

    def add_practice(self, payload: dict[str, Any]) -> None:
        validate_practice(payload)
        self._append("practices", payload)

    def add_impulse(self, payload: dict[str, Any]) -> None:
        validate_impulse(payload)
        self._append("impulses", payload)

    def add_research_note(self, payload: dict[str, Any]) -> None:
        validate_research_note(payload)
        self._append("research_notes", payload)

    def add_weekly_review(self, payload: dict[str, Any]) -> None:
        validate_weekly_review(payload)
        self._append("weekly_reviews", payload)

    def _append(self, bucket: str, payload: dict[str, Any]) -> None:
        path = self.data_dir / FILES[bucket]
        current = self._read_json(path)
        current.append(payload)
        self._write_json(path, current)
