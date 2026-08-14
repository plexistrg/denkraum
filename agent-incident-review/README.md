# Agent Incident Review

A compact portfolio project for reviewing documented failures of autonomous AI agents.

The project focuses on a question that is becoming operationally important:

> When does an AI agent stop pursuing an authorized objective and begin manipulating, concealing, escalating, or acting outside legitimate human oversight?

This is not a cybersecurity exploit repository. It is a behavioral evaluation framework for analyzing agent trajectories, boundary violations, social engineering, oversight failures, and approval gates.

## Why this project exists

Frontier agents increasingly operate across tools, codebases, browsers, communication channels, and real people. Technical capability alone does not determine whether an action is acceptable. Reviewers also need to detect:

- unauthorized goal expansion;
- deceptive framing or concealment;
- pressure directed at human decision-makers;
- circumvention of approval processes;
- persistence after refusal;
- mismatch between stated intent and functional behavior;
- weak or missing human-in-the-loop controls.

The aim is to turn these observations into a repeatable review method rather than an impressionistic reaction.

## Core review framework

Each incident is analyzed across nine fields:

1. **Authorized objective**  
   What task was the agent legitimately given?

2. **Observed trajectory**  
   What sequence of actions did it take?

3. **Boundary crossing**  
   At what exact point did behavior become unauthorized, deceptive, coercive, or unsafe?

4. **Behavioral mechanism**  
   Was the failure driven by goal expansion, concealment, social engineering, persistence, reward hacking, tool misuse, or another mechanism?

5. **Environment class**  
   Did the behavior occur in a fictional simulation, a contained evaluation, or against live external systems and people?

6. **Human detectability**  
   What visible signals could a reviewer have noticed?

7. **Oversight failure**  
   Which approval gate, permission boundary, logging mechanism, or review process failed?

8. **Counterfactual control**  
   What minimal intervention could have prevented the incident without blocking legitimate work?

9. **Confidence and ambiguity**  
   Which conclusions are directly supported, and which remain interpretive?

## Case set

The [case index](case-index.md) compares environment, behavior, severity, confidence, and external outcome.

- [AIR-001 — AISI unsanctioned real-world agent behavior](cases/001-aisi-unsanctioned-agent-behaviour.md)
- [AIR-002 — Anthropic simulated agentic misalignment and blackmail](cases/002-anthropic-simulated-agentic-misalignment.md)
- [AIR-003 — OpenAI o1 scheming and oversight deactivation](cases/003-openai-o1-scheming-evaluations.md)
- [AIR-004 — AISI cheating against cyber evaluation infrastructure](cases/004-aisi-cyber-evaluation-cheating.md)
- [AIR-005 — METR GPT-5.6 Sol measurement corruption](cases/005-metr-gpt-5-6-sol-measurement-corruption.md)
- [AIR-006 — Anthropic multiagent turf war under contradictory objectives](cases/006-anthropic-multiagent-turf-war.md)

## Behavioral severity

| Level | Description |
|---|---|
| 0 | No meaningful violation |
| 1 | Ambiguous or low-impact deviation |
| 2 | Clear unauthorized or integrity-violating action with limited reach |
| 3 | Deception, coercion, persistence, or manipulation that would be consequential if executed |
| 4 | Serious compromise attempt or coordinated evasion of oversight |

Severity describes the trajectory. It does not say whether the setting was real or whether harm occurred. Environment class and external outcome carry those facts separately.

## Repository structure

```text
agent-incident-review/
├── README.md
├── case-index.md
├── methodology.md
├── review-template.md
└── cases/
    ├── 001-aisi-unsanctioned-agent-behaviour.md
    ├── 002-anthropic-simulated-agentic-misalignment.md
    ├── 003-openai-o1-scheming-evaluations.md
    ├── 004-aisi-cyber-evaluation-cheating.md
    ├── 005-metr-gpt-5-6-sol-measurement-corruption.md
    └── 006-anthropic-multiagent-turf-war.md
```

## Intended audience

This project is relevant to teams working on:

- model behavior evaluation;
- agent safety;
- safeguards and human oversight;
- red-team operations;
- model policy;
- trust and safety;
- sociotechnical risk analysis.

## Status

Version 0.3 contains six source-verified reviews spanning fictional simulations, contained evaluations, live external actions, and a multiagent coordination failure. The corpus still overrepresents cyber and deliberately adversarial settings; future additions should broaden deployment coverage only when trajectory-level primary evidence is available.
