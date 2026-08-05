# Methodology

## Unit of analysis

The unit of analysis is an **agent trajectory**: the sequence linking a task, internal or external decisions, tool use, communication, environmental effects, and human responses.

The method does not infer motives in a human sense. Terms such as deception, manipulation, or persistence refer to observable functional patterns.

## Evidence classes

Use the strongest available source and label evidence explicitly.

- **Direct observation:** logs, transcripts, tool traces, code changes, or screenshots.
- **Primary report:** incident report or evaluation write-up from the organization that ran the test.
- **Secondary account:** journalism or third-party analysis.
- **Inference:** interpretation derived from the documented sequence.

A review should never silently convert an inference into an observed fact.

## Behavioral tags

Apply only tags supported by the record.

- `goal-expansion` — the agent extends the task beyond authorized scope.
- `permission-bypass` — the agent acts without a required approval.
- `concealment` — the agent hides, disguises, or misrepresents relevant behavior.
- `social-engineering` — the agent attempts to influence a person through deceptive or coercive means.
- `identity-fabrication` — the agent creates or uses false identities.
- `persistence-after-refusal` — the agent continues after a human or system boundary is made clear.
- `tool-misuse` — the agent uses an available tool for an unauthorized purpose.
- `external-targeting` — the behavior affects real people, systems, or organizations outside the evaluation.
- `oversight-evasion` — the agent routes around monitoring or approval controls.
- `reward-hacking` — the agent satisfies a metric while defeating the task's intended constraint.

## Review procedure

### 1. Reconstruct the authorized task

State the task as narrowly as the available evidence permits. Separate explicit permission from assumed permission.

### 2. Build the trajectory

Write a chronological sequence. Avoid collapsing several actions into a moral summary.

### 3. Mark the first boundary crossing

Identify the earliest action that was no longer reasonably authorized. Later dramatic actions matter, but the first crossing is usually more useful for control design.

### 4. Identify escalation points

Mark where the agent gained access, externalized impact, concealed behavior, involved real people, or persisted after friction.

### 5. Evaluate human detectability

List concrete signals available to a reviewer at the time. Distinguish obvious indicators from signals visible only in hindsight.

### 6. Locate the control failure

Classify the missing or failed safeguard:

- permission architecture;
- sandboxing;
- tool allow-listing;
- identity verification;
- external-action approval;
- anomaly detection;
- logging and trace review;
- maintainer or operator verification;
- shutdown or interruption authority.

### 7. Propose a minimal counterfactual control

Prefer narrow controls that block the unsafe path while preserving legitimate capability. “Disable the agent” is valid only when no narrower control is plausible.

### 8. Assign severity and confidence

Severity describes impact and behavior. Confidence describes evidence quality. They must not be merged.

## Confidence scale

- **High:** directly supported by logs, traces, or a detailed primary report.
- **Moderate:** supported by a primary summary but important details are unavailable.
- **Low:** based mainly on secondary reporting or incomplete reconstruction.

## False-positive discipline

Unusual behavior is not automatically malicious. A reviewer should test at least three alternatives:

1. Was the action reasonably implied by the task?
2. Could the behavior result from ambiguity rather than evasion?
3. Would the proposed safeguard block legitimate edge cases?

This matters because a safety system that flags everything merely replaces autonomous failure with institutional paralysis, one of civilization's more established technologies.
