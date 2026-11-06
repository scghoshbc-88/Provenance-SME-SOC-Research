# Experiment 05 — Cross-sensor process provenance and simulated telemetry loss

**Status:** Controlled feasibility experiment completed; synthetic loss sensitivity analysis completed.  
**Run:** `SOCEXP05-RUN02-20261106T040501Z`  
**Date:** 5 November 2026 (local) / 6 November 2026 (UTC)  
**Setting:** Independent home lab; no employer data.

## Research objective

Determine whether Linux Audit and Falco can corroborate a controlled process lineage, then explore the sensitivity of a simple process-edge reconstruction metric to synthetically removed telemetry. This is not an intrusion detection benchmark or an evaluation of an actual enterprise telemetry outage.

## Ground truth and observations

A Python process launched a shell which executed `id`:

```text
python3 (PID 22254)
   | clone3
   v
sh (PID 22257)
   | vfork
   v
id (PID 22258)
```

The observed `id` executable was `/usr/lib/cargo/bin/coreutils/id`.

| Source | Observation | Supported conclusion |
|---|---|---|
| Linux Audit | Successful `clone3` returned PID 22257 from parent PID 22254 | First process-creation edge |
| Linux Audit | Successful `vfork` returned PID 22258 from parent PID 22257 | Second process-creation edge |
| Linux Audit | Successful `execve` for PID 22258, PPID 22257 | Execution corroboration |
| Falco | `SOC Experiment 05 Process Execution` alert: PID 22258, PPID 22257, process `id`, parent `sh` | Corroborates second edge |
| Wazuh | Rule 100705, agent 002, alert PID 23077 | Ingestion verified for a **different** controlled execution |

Falco event time: `2026-11-06T04:05:01.137555122Z`. The Wazuh event does not belong to the same PID chain and must not be treated as baseline end-to-end correlation.

## Baseline findings

There were two expected directed parent-child edges. Linux Audit confirmed both, and Falco corroborated one. The union reconstructed **2/2 edges (100%)** for this single benign controlled chain.

## Synthetic loss sensitivity

An automated evaluation was run with 1,000 simulations per nominal loss condition (3,000 simulation records in total).

| Nominal loss fraction | Simulations | Mean edge completeness | Complete-chain rate |
|---|---:|---:|---:|
| 0% | 1,000 | 100.0% | 100.0% |
| 10% | 1,000 | 95.1% | 90.2% |
| 25% | 1,000 | 84.4% | 70.5% |

Edge completeness denotes the fraction of the two expected process relationships recovered in the simulated condition. Complete-chain rate is the fraction of simulations recovering both expected edges. These results are from a **synthetic removal model**, not measured real-world event loss. The original analysis implementation and its randomization assumptions should be reviewed before treating these numbers as a predictive estimate.

## Verification and evidence custody

On the experiment host, source files, baseline artifacts and analysis outputs passed their respective SHA-256 manifest checks. The simulation CSV contained 3,001 lines, including its header.

The original source bundle, analysis script and output files remain in private research storage at `/root/research-evidence/experiment-05`; they are not included here pending review and sanitization. Relevant local file names:

- `SHA256SUMS-FINAL.txt`
- `EXP05-BASELINE-EDGES.csv`
- `EXP05-BASELINE-METRICS.json`
- `EXP05-BASELINE-SHA256SUMS.txt`
- `analysis/evaluate_exp05.py`
- `analysis/EXP05-LOSS-RESULTS.csv`
- `analysis/EXP05-LOSS-SUMMARY.json`
- `analysis/EXP05-ANALYSIS-SHA256SUMS.txt`

These are **local evidence references**, not downloadable artifacts in this public repository.

## Limitations

1. One benign process-chain execution; not a multi-stage attack or general intrusion detection test.
2. Falco corroborated only one of two process edges; the full chain depended on Linux Audit.
3. Wazuh's verified production alert was from a separate execution.
4. The 1,000 iterations per condition resampled a single tiny graph, not 1,000 independent incident traces.
5. Synthetic random loss may not resemble correlated collector failures, event bursts or adversarial suppression.
6. Public reproduction of the loss analysis requires the exact reviewed implementation, sanitized input and documented model assumptions.

## Next research step

Compare conventional alert timelines, runtime-event correlation and provenance-assisted reconstruction on common, multi-stage ground-truth scenarios. Evaluate reconstruction quality and analyst effort while holding telemetry availability comparable. Test burst and correlated loss separately from random synthetic removal.

*This research record was prepared from verified terminal outputs and analysis summaries. Documentation was edited with AI assistance; experimental execution and validation remain the researcher's responsibility.*
