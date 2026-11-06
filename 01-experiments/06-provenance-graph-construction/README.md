# Experiment 06: Provenance Graph Construction

## Objective

Evaluate whether process-creation telemetry collected in a
controlled Linux environment can be reconstructed into a
directed provenance graph and independently corroborated
using Falco runtime events.

## Source Evidence

Experiment 05, Run 02

Run ID: SOCEXP05-RUN02-20261106T040501Z

Telemetry sources:
- Linux Audit
- Falco runtime detection

A separate Wazuh production alert was preserved during
Experiment 05 but was not correlated to this execution.

## Methodology

A controlled process chain was executed:

python3 (PID 22254)
  -> sh (PID 22257)
      -> id (PID 22258)

Linux Audit records were examined to identify successful
process-creation syscalls and reconstruct parent-child edges.

A directed graph was constructed using NetworkX and
exported to GraphML.

Falco JSON telemetry was then correlated using process
identifiers and parent-process identifiers.

## Results

| Metric | Result |
|---|---|
| Process nodes | 3 |
| Expected process edges | 2 |
| Reconstructed process edges | 2 |
| Linux Audit verified edges | 2 |
| Falco corroborated edges | 1 |
| Process-edge completeness | 100% |
| Falco edge corroboration | 50% |
| Directed acyclic graph | Yes |

The verified process relationships were:

1. python3 -> sh, supported by clone3.
2. sh -> id, supported by vfork.

Falco independently corroborated the second relationship
through execution metadata.

## Interpretation

Linux Audit provided sufficient process-creation evidence
to reconstruct both expected relationships in this
single controlled execution.

Falco supplied independent corroborating evidence for
the shell-to-id relationship.

These findings demonstrate feasibility of process-level
provenance reconstruction for this specific scenario.

## Limitations

- Only one controlled process chain was evaluated.
- No process-file or process-network relationships were tested.
- Falco corroboration covered one of two process edges.
- Wazuh was not verified against the same execution.
- No attack-detection precision or recall was measured.
- No live telemetry-loss experiment was conducted.
- The results cannot establish general performance across
  different workloads or attack scenarios.

## Reproducibility

The repository includes:

- Graph construction source code.
- Original reconstructed GraphML.
- Falco-correlated GraphML.
- Graph visualization.
- Correlation metrics.
- SHA-256 integrity manifest.

The graph is derived from Experiment 05 Run 02 evidence.

## Research Status

Experiment 06 process-graph construction and correlation:
Completed for the controlled baseline scenario.

Further experiments are required for multi-stage attack
reconstruction, process-file-network relationships,
telemetry-loss robustness, and comparative evaluation.
