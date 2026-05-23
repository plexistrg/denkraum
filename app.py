from __future__ import annotations

import streamlit as st

from src.storage import LocalStore

st.set_page_config(page_title="Denkraum Studio v0.1", page_icon="🛠️", layout="centered")

store = LocalStore()

STRICT_PROMPTS = [
    "Is this practice or only talk?",
    "What is the next grip?",
    "Can Nina see, hear, touch, or imitate this?",
    "Is this baubar?",
]

VAGUE_TOKENS = {
    "maybe",
    "later",
    "sometime",
    "think",
    "should",
    "try",
    "idea",
    "concept",
    "better",
}


def strict_vagueness_check(values: list[str]) -> list[str]:
    lowered = " ".join(values).lower()
    return [token for token in sorted(VAGUE_TOKENS) if token in lowered]


st.title("Denkraum Studio v0.1")
st.caption("Friction → Form → Next Action")

strict_mode = st.toggle("Strict Mode", value=False)
if strict_mode:
    st.warning("Strict mode is enabled. Vague language gets challenged.")
    for prompt in STRICT_PROMPTS:
        st.write(f"- {prompt}")

mode = st.radio("Entry mode", ["Jetzt beruhigen", "Jetzt vertiefen", "Jetzt bauen"])
mode_map = {
    "Jetzt beruhigen": "beruhigen",
    "Jetzt vertiefen": "vertiefen",
    "Jetzt bauen": "bauen",
}

st.divider()

st.subheader("Start in 10 seconds")
mode_practices = [p for p in store.list_items("practices") if p["mode"] == mode_map[mode]]
if mode_practices:
    starter = mode_practices[0]
    st.success(
        f"Now: **{starter['concrete_first_action']}**  \\\nRepeat cue: {starter['next_repetition_cue']}"
    )
    st.caption(
        f"Nina now: {starter['nina_version']} | Shared now: {starter['shared_parent_child_version']}"
    )

st.divider()
st.subheader("Practice Library")
if mode_practices:
    for p in mode_practices:
        with st.expander(p["title"]):
            st.write(f"**First action now:** {p['concrete_first_action']}")
            st.write(f"**Duration:** {p['duration']}")
            st.write(f"**Trigger:** {p['trigger']}")
            st.write(f"**Failure mode:** {p['failure_mode']}")
            st.write(f"**Repeat cue:** {p['next_repetition_cue']}")
            st.write(f"**Adult:** {p['adult_version']}")
            st.write(f"**Nina:** {p['nina_version']}")
            st.write(f"**Shared parent-child:** {p['shared_parent_child_version']}")
else:
    st.info("No practices for this mode yet.")

st.divider()
st.subheader("Impulse Capture (under 60 seconds)")
with st.form("impulse_form", clear_on_submit=True):
    what_appeared = st.text_area("What appeared?*", placeholder="One short line.")
    concrete_action = st.text_area(
        "What is the concrete movement/action?*",
        placeholder="Body move or visible action only.",
    )
    next_step = st.text_area("What is the next tiny build step?*", placeholder="Single tiny step in <2 minutes.")
    submitted = st.form_submit_button("Save impulse")
    if submitted:
        payload = {
            "what_appeared": what_appeared,
            "concrete_movement_action": concrete_action,
            "next_tiny_build_step": next_step,
        }
        if strict_mode:
            flagged = strict_vagueness_check(list(payload.values()))
            if flagged:
                st.error(f"Too vague for strict mode. Remove fuzzy words: {', '.join(flagged)}")
                st.stop()
        try:
            store.add_impulse(payload)
            st.success("Impulse saved.")
        except ValueError as exc:
            st.error(str(exc))

st.divider()
st.subheader("Research Notes")
with st.form("research_form", clear_on_submit=True):
    source_title = st.text_input("Source/title*", placeholder="Book, article, or talk title")
    insight = st.text_area("One-sentence insight*", placeholder="One sentence only.")
    practice_translation = st.text_area(
        "Practice translation*", placeholder="Exactly what to do in the body/environment."
    )
    open_question = st.text_area("Open question*", placeholder="Only one question.")
    submitted_research = st.form_submit_button("Save research note")
    if submitted_research:
        payload = {
            "source_title": source_title,
            "one_sentence_insight": insight,
            "practice_translation": practice_translation,
            "open_question": open_question,
        }
        if strict_mode:
            flagged = strict_vagueness_check([payload["practice_translation"], payload["one_sentence_insight"]])
            if flagged:
                st.error(f"Strict mode: translate this into executable practice, not talk: {', '.join(flagged)}")
                st.stop()
        try:
            store.add_research_note(payload)
            st.success("Research note saved.")
        except ValueError as exc:
            st.error(str(exc))

st.divider()
st.subheader("Weekly Review (under 3 minutes)")
with st.form("review_form", clear_on_submit=True):
    pulled = st.text_area("What pulled me in?*", placeholder="One bullet-style line.")
    dead = st.text_area("What stayed dead?*", placeholder="What got no movement?")
    repeat = st.text_area("What should repeat next week?*", placeholder="Repeat only what worked in body/time.")
    remove = st.text_area("What should be removed?*", placeholder="Delete one drag or dead routine.")
    submitted_review = st.form_submit_button("Save weekly review")
    if submitted_review:
        payload = {
            "what_pulled_me_in": pulled,
            "what_stayed_dead": dead,
            "what_should_repeat_next_week": repeat,
            "what_should_be_removed": remove,
        }
        try:
            store.add_weekly_review(payload)
            st.success("Weekly review saved.")
        except ValueError as exc:
            st.error(str(exc))
