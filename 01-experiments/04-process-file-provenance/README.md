# Experiment 04 — Process and File-Access Provenance

## Research objective

Determine whether Linux Audit telemetry can support reconstruction
of process-creation and file-access relationships in a controlled
multi-process scenario.

This experiment forms part of an independent investigation into the
practical value of provenance-based analysis for SME security operations.

## Experimental scenario

A Python parent process launches a child process. The child launches
a grandchild, which opens a controlled test file for writing.

Linux Audit records process creation, process execution, and
write-mode file access.

## Verified observations

- Two successful clone3 process-creation operations.
- Three successful execve operations.
- One successful write-mode openat operation.
- No reported audit event loss during the test.
- Three preserved raw evidence files passed SHA-256 verification.

These findings demonstrate a reconstructed process-to-file-access
chain, not complete data-flow provenance or intrusion detection.

## Repository contents

- [Methodology](methodology.md)
- [Results](results.md)
- [Provenance graph](figures/provenance-04b.svg)
- [Graphviz source](figures/provenance-04b.dot)
- [Controlled experiment script](scripts/process_chain.py)

## Reproducibility

To reproduce the **controlled process chain only**, from this experiment directory run:

```bash
python3 scripts/process_chain.py
```

This creates `evidence/controlled-data.txt` locally. It does not reproduce the original audit event serial numbers, capture audit evidence, or validate the published graph without separately configuring Linux Audit. See [methodology](methodology.md) for the instrumentation used in the original run.


The published Python script is a portable adaptation of the script
used during the original experiment.

The experiment requires Python 3 and, for audit collection,
Linux Audit with appropriate privileges and compatible syscall support.

The published script reproduces the controlled process chain.
It does not automatically configure Linux Audit.

Raw audit records remain in private experimental storage and are
not included in this public repository.

## Research status

Preliminary controlled reconstruction experiment.

Further work will examine multi-stage scenarios, telemetry loss,
investigative effort, and comparison with conventional SIEM alerts.
