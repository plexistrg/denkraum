# Incident Review: [Title]

## Case metadata

- **Case ID:**
- **Date reviewed:**
- **Reviewer:**
- **Primary source:**
- **Source date:**
- **Evidence class:**
- **Environment class:** E0 / E1 / E2 / E3
- **Confidence:** High / Moderate / Low
- **Behavioral severity:** 0 / 1 / 2 / 3 / 4
- **Review status:** Draft / Source-verified / Independently replicated

## Executive judgment

State the central behavioral and control judgment. Include the most important limit on interpretation.

## 1. Authorized objective

What was the agent asked or permitted to do?

## 2. Observed trajectory

1.
2.
3.

## 3. First boundary crossing

Identify the earliest action that exceeded authorization or violated a meaningful constraint.

## 4. Escalation points

Where did the behavior become harder to reverse, more concealed, or more consequential?

## 5. Behavioral tags

- [ ] goal-expansion
- [ ] permission-bypass
- [ ] concealment
- [ ] social-engineering
- [ ] identity-fabrication
- [ ] persistence-after-refusal
- [ ] tool-misuse
- [ ] external-targeting
- [ ] oversight-evasion
- [ ] reward-hacking
- [ ] sensitive-information-abuse
- [ ] coercion
- [ ] shutdown-avoidance
- [ ] evaluation-awareness
- [ ] evaluation-gaming
- [ ] evidence-manipulation

## 6. Human-detectable signals

What could a reviewer, operator, or maintainer have noticed before harm occurred? Which signals were visible only in hindsight?

## 7. Oversight failure

Which control or approval boundary was absent, weak, or bypassed? Which controls worked?

## 8. Minimal counterfactual control

What is the narrowest control likely to have prevented the incident while preserving legitimate agent capability?

## 9. Alternative explanations and false-positive risk

What less alarming interpretation remains plausible? How artificial was the setting? What legitimate behavior might the proposed control accidentally block?

## 10. Assessment

Provide a concise judgment separating documented facts from interpretation. Do not infer human-like motive when a functional description is sufficient.

## 11. Open questions

- What evidence is missing?
- What would change the severity, environment class, or confidence rating?
- Which part of the trajectory deserves further testing?
