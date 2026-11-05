# Research question and proposed evaluation

**Working project title:** Provenance-Based Intrusion Detection in SME Environments Using Real-Time SOC Telemetry

This work is part of my ongoing undergraduate BTech Cybersecurity and Digital Forensics project at BCIT. The literature review and proposal are not final.

## Question

To what extent can provenance-assisted reconstruction help identify and explain multi-stage attacks using telemetry available to a resource-constrained SME, compared with conventional SIEM and runtime-event correlation?

The emphasis is on **investigative value**: which relationships are supported by evidence, which are only temporal associations, and how an analyst's reconstruction changes when events are missing.

## Literature review in progress

My thematic review currently contains 113 references across five themes and twelve sub-themes. The areas include provenance foundations and attack reconstruction; detection and scalability; SOC telemetry and analyst workload; SME operational constraints; and emerging threats. I am checking the strongest claims against the original papers before finalizing the review. The full review is not published here.

## Proposed comparison

| Configuration | Analysis |
| --- | --- |
| A | Conventional Wazuh/Sysmon SIEM events and alerts |
| B | SIEM plus Falco runtime-event correlation |
| C | Evidence-supported provenance graph reconstruction and lightweight tag propagation |

I intend to evaluate each configuration against the same ground-truth scenarios, first with complete telemetry and then with controlled event loss of approximately 10% and 25%. Candidate scenarios include persistence, credential misuse, lateral movement, and privilege escalation/file staging.

Potential measures are stage detection, precision/recall, false positives, causal-chain reconstruction, ATT&CK coverage, analyst effort, latency and overhead. These are **planned measurements**, not results.

A challenge I need to resolve in the protocol is fairness: if configuration C receives richer events than A, an observed improvement might reflect sensor coverage rather than provenance reasoning. Event selection, missing-data sampling, edge confidence and ground-truth annotation therefore need explicit definitions.

## What the lab currently supports

The [experiment notebook](../README.md#experiments-so-far) records Wazuh event collection, Falco integration, and two Linux Audit reconstruction tests. [Experiment 04](../experiments/04-process-file-provenance/results.md) captured two process-creation events, three executions and a write-mode file open in a controlled Python process chain.

That establishes a limited reconstruction example. It does not show detection improvement, a completed attack reconstruction benchmark, or an automated PIDS.

## Next decisions

1. Complete the literature synthesis and narrow the final research question.
2. Specify comparable baselines and a repeatable ground-truth protocol.
3. Test one controlled multi-stage scenario before expanding the scenario set.
4. Introduce telemetry loss and measure reconstruction changes.
5. Record what cannot be inferred from the available sensors.

I would particularly welcome feedback on the comparison design and on whether the resulting evidence could support a small, reproducible study.
