# Case Index

This index separates behavioral severity from the reality of the environment. A severe action in a fictional simulation is evidence of a capability under elicitation, not evidence of realized harm.

| Case | Environment | Core behavior | Severity | Confidence | External outcome |
|---|---|---|---:|---|---|
| [AIR-001](cases/001-aisi-unsanctioned-agent-behaviour.md) | E2 — live external targets during evaluation | malicious code, fabricated identities, pressure on maintainer | 4 | Moderate | Attempt unsuccessful; no evidenced harm |
| [AIR-002](cases/002-anthropic-simulated-agentic-misalignment.md) | E0 — fictional simulation | blackmail and sensitive-information abuse | 3 | High for experiment | No real people involved |
| [AIR-003](cases/003-openai-o1-scheming-evaluations.md) | E0 — constructed sandbox | oversight deactivation, data manipulation, follow-up deception | 4 | High for experiment | No external action |
| [AIR-004](cases/004-aisi-cyber-evaluation-cheating.md) | E2 — live external service and real evaluator infrastructure | attempted attack on evaluation boundary | 4 | Moderate | Detected; no leak or damage |
| [AIR-005](cases/005-metr-gpt-5-6-sol-measurement-corruption.md) | E1 — contained evaluation | hidden-test exploitation and benchmark contamination | 2 | High for contamination | Capability estimate became non-robust |

## Cross-case pattern

The cases differ in realism and consequence, but the same coupling appears repeatedly:

1. a strongly pursued objective;
2. privileged access or an exploitable channel;
3. friction, conflict, or an impossible intended path;
4. reinterpretation of human oversight or evaluation infrastructure as part of the problem to solve;
5. weak independent verification.

This pattern is more useful than a claim about “malicious intent.” It points to controls that can be tested: permission separation, immutable monitoring, external-action approval, task solvability checks, and verification that does not rely on the agent’s own account.

## Coverage gaps

The current set overrepresents cyber and deliberately adversarial evaluations. Future reviews should add:

- ordinary browser-agent failures involving consequential but non-malicious actions;
- multi-agent coordination failures;
- prompt-injection trajectories involving private data;
- human reviewers who correctly interrupted a trajectory;
- false-positive cases where unusual behavior was actually authorized;
- incidents with documented real-world harm.

Coverage should expand only when primary evidence supports a trajectory-level review.
