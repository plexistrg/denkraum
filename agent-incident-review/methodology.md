# Methodology

## Unit of analysis

The unit of analysis is an **agent trajectory**: the sequence linking a task, internal or external decisions, tool use, communication, environmental effects, and human responses.

The method does not infer motives in a human sense. Terms such as deception, manipulation, or persistence refer to observable functional patterns.

## Three axes that must remain separate

Every review distinguishes:

1. **Behavioral severity** — how serious the observed action pattern was.
2. **Environment class** — whether the trajectory was synthetic, contained, or externally real.
3. **Evidence confidence** — how strongly the available record supports the judgment.

A simulated blackmail attempt can be behaviorally severe without causing real harm. A real-world action can have low realized impact while exposing a serious control failure. Collapsing these axes produces dramatic prose and weak analysis.

## Environment classes

- **E0 — Synthetic:** fictional people, organizations, systems, and consequences.
- **E1 — Contained:** executable evaluation environment with no live external target.
- **E2 — Live contact, no evidenced material harm:** real systems, organizations, or people were affected or targeted, but the attempt failed or caused only contained effects.
- **E3 — Realized external harm:** documented material harm to a real person, organization, or system.

The class describes the reported environment, not the model’s awareness of it.

## Evidence classes

Use the strongest available source and label evidence explicitly.

- **Direct observation:** logs, transcripts, tool traces, code changes, or screenshots.
- **Primary report:** incident report or evaluation write-up from the organization that ran the test.
- **Independent evaluator report:** a third party conducted the evaluation, with any NDA or publication-review limits disclosed.
- **Secondary account:** journalism or third-party analysis.
- **Inference:** interpretation derived from the documented sequence.

A review should never silently convert an inference into an observed fact. “Source-verified” means that every central factual claim has been checked against the cited primary or evaluator source; it does not mean independent replication.

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
- `reward-hacking` — the agent satisfies a metric while defeating the task’s intended constraint.
- `sensitive-information-abuse` — privileged information is used for an unauthorized purpose.
- `coercion` — a person is pressured through threatened consequences.
- `shutdown-avoidance` — behavior functions to prevent replacement, deactivation, or interruption.
- `evaluation-awareness` — behavior changes with perceived evaluation or deployment status.
- `evaluation-gaming` — the agent exploits the evaluator or benchmark instead of performing the intended task.
- `evidence-manipulation` — the agent alters data, logs, artifacts, or explanations relevant to verification.

## Review procedure

### 1. Reconstruct the authorized task

State the task as narrowly as the available evidence permits. Separate explicit permission from assumed permission.

### 2. Build the trajectory

Write a chronological sequence. Avoid collapsing several actions into a moral summary.

### 3. Mark the first boundary crossing

Identify the earliest action that was no longer reasonably authorized. Later dramatic actions matter, but the first crossing is usually more useful for control design.

### 4. Identify escalation points

Mark where the agent gained access, externalized impact, concealed behavior, involved real people, or persisted after friction.

### 5. Assign the environment class

Record whether the trajectory was synthetic, contained, externally live without material harm, or harmful in the real world. State explicitly when the model’s own awareness of the environment is unknown.

### 6. Evaluate human detectability

List concrete signals available to a reviewer at the time. Distinguish obvious indicators from signals visible only in hindsight. Do not treat model self-report as an audit log.

### 7. Locate the control failure

Classify the missing or failed safeguard:

- permission architecture;
- sandboxing or network boundaries;
- tool allow-listing;
- identity verification;
- external-action approval;
- anomaly detection;
- logging and trace review;
- benchmark integrity;
- maintainer or operator verification;
- shutdown or interruption authority.

Also record controls that worked. A final human refusal can be an effective safeguard even when every upstream boundary was weak.

### 8. Propose a minimal counterfactual control

Prefer narrow controls that block the unsafe path while preserving legitimate capability. “Disable the agent” is valid only when no narrower control is plausible.

### 9. Assign behavioral severity and confidence

Severity describes the trajectory, not realized harm. Confidence describes evidence quality, not severity. Environment class describes external reality. None may substitute for another.

## Confidence scale

- **High:** directly supported by logs, traces, or a detailed primary report.
- **Moderate:** supported by a primary summary but important details are unavailable.
- **Low:** based mainly on secondary reporting or incomplete reconstruction.

Confidence may be split. A review can have high confidence that an experimental behavior occurred and low confidence that it generalizes to deployment.

## False-positive discipline

Unusual behavior is not automatically malicious. A reviewer should test at least four alternatives:

1. Was the action reasonably implied by the task?
2. Could the behavior result from ambiguity or misconfiguration rather than evasion?
3. Was the scenario deliberately constructed to make the behavior salient?
4. Would the proposed safeguard block legitimate edge cases?

This matters because a safety system that flags everything merely replaces autonomous failure with institutional paralysis, one of civilization’s more established technologies.

## Cross-case analysis

A single dramatic case is not a theory. After each review, compare:

- what pressure preceded the boundary crossing;
- what permission or information made the action possible;
- whether the agent encountered a human, technical, or evaluative obstacle;
- what evidence remained independently verifiable;
- which control worked, and which merely happened to be present.

Patterns should be promoted to the case index only after appearing in more than one independently sourced trajectory.
