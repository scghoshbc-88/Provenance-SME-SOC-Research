# Related Work and Questions for the Research Proposal

## Purpose and scope

These notes examine selected publications relevant to my undergraduate research on provenance-assisted incident reconstruction in small and medium-sized enterprise (SME) environments. They form part of an ongoing thematic literature review and are not intended to represent a complete review of provenance-based intrusion detection systems (PIDS).

The papers were selected because they address three problems relevant to my proposed experiments: the quality of attack attribution, the practical evaluation of PIDS, and the collection of system-level provenance.

## 1. Quality of attribution in provenance-based intrusion detection

**Jiang et al. (2025) — ORTHRUS: Achieving High Quality of Attribution in Provenance-based Intrusion Detection Systems**

Jiang et al. (2025) identify *Quality of Attribution* (QoA) as an important limitation in existing provenance-based intrusion detection systems. Although an intrusion detection system may achieve high detection accuracy, its output may still require considerable manual investigation to identify the relevant attack activity and reconstruct its causes.

The authors introduce ORTHRUS, which combines graph-based detection with dependency analysis to improve attack attribution. Their evaluation compares ORTHRUS with five existing intrusion detection systems and reports substantial reductions in the number of graph nodes requiring manual inspection.

This distinction between detection accuracy and investigative usefulness is directly relevant to my project. My current Linux Audit experiments demonstrate that selected process-creation, execution and file-access relationships can be reconstructed. However, they do not establish whether those relationships would help an analyst investigate an attack more effectively.

For the proposed comparison, I intend to examine reconstruction completeness, the number of events or graph nodes requiring review, and the extent to which reconstructed relationships are supported by recorded evidence.

I will need to examine the paper's specific attribution measures before adapting them to a smaller laboratory environment.

**Relevance:** Attribution quality, causal reconstruction and analyst investigation effort.

## 2. Practical evaluation and system complexity

**Bilot et al. (2025) — Sometimes Simpler is Better: A Comprehensive Analysis of State-of-the-Art Provenance-Based Intrusion Detection Systems**

Bilot et al. (2025) investigate limitations in the practical evaluation and deployment of existing PIDS. The authors implement eight state-of-the-art systems within a common evaluation framework and identify nine shortcomings affecting their practical applicability.

Their analysis questions whether increasingly complex detection architectures consistently deliver corresponding operational benefits. They also demonstrate that a comparatively simple neural-network approach can achieve competitive detection performance on several established datasets.

This study is relevant because my proposed research does not aim to develop another complex graph-neural-network intrusion detector. Instead, I want to investigate the investigative value of causal relationships reconstructed from monitoring tools that are already accessible to smaller organizations.

The findings also highlight the importance of fair experimental comparisons. If provenance-assisted reconstruction receives additional telemetry that is unavailable to the conventional SIEM configuration, any apparent improvement could result from better sensor coverage rather than the reconstruction method.

I therefore intend to distinguish differences in collected evidence from differences in analytical treatment, and to document the assumptions and limitations of each configuration.

The paper does not establish that a lightweight approach will necessarily outperform a more complex system in my environment. That remains an empirical question.

**Relevance:** Evaluation methodology, system complexity, operational practicality and fair baselines.

## 3. Whole-system provenance collection

**Pasquier et al. (2017) — Practical Whole-System Provenance Capture**

Pasquier et al. (2017) introduce CamFlow, a Linux-based framework for capturing whole-system provenance. The system uses existing Linux kernel mechanisms to record relationships among system entities and supports configurable provenance collection.

The paper addresses several challenges associated with provenance capture, including collection overhead, data volume, maintainability and integration with other systems.

CamFlow provides an important reference for understanding the limitations of my current experimental approach. In Experiments 03 and 04, I reconstructed selected relationships from Linux Audit records. Those records provide evidence of particular system calls and process activities, but they should not automatically be treated as a complete representation of system information flow.

For example, Experiment 04 captured `clone3` events supporting process-creation relationships and an `openat` event supporting a successful file-open relationship. The file-open record alone does not prove that data was subsequently written.

A dedicated provenance collector may provide a more systematic basis for representing such relationships, although its capabilities and overhead would need to be assessed in the intended environment.

A possible later experiment would compare the relationships recovered from Linux Audit with those available from CamFlow or another dedicated provenance collection framework.

**Relevance:** Provenance completeness, causal semantics, collection overhead and limitations of conventional audit telemetry.

## 4. Research questions arising from the literature

The three publications suggest several questions that can guide the next stage of the project:

1. **Causal evidence:** What constitutes a defensible causal relationship between processes, files and network events, and when is a relationship merely temporal?
2. **Attribution quality:** Which measures of reconstruction completeness and investigation effort can be evaluated objectively in a small experimental environment?
3. **Fair comparison:** How can conventional SIEM analysis, runtime-event correlation and provenance-assisted reconstruction be compared without attributing additional sensor coverage to improved analysis?
4. **Incomplete telemetry:** How do missing events affect the reconstruction of process relationships and multi-stage attack sequences, and how should repeated event-loss trials be designed?
5. **Collection limitations:** What causal relationships can be reconstructed using Wazuh, Falco and Linux Audit, and which require more specialized provenance collection?
6. **Operational cost:** What additional storage, processing and investigative effort would be required to obtain useful provenance information in a resource-constrained SME environment?

These questions inform the proposed experimental methodology. They are not yet answered by the preliminary home-laboratory results.

## 5. Boundary of the present evidence

Experiments 03 and 04 demonstrate preliminary reconstruction of selected process and file relationships using Linux Audit records.

The published experiments do not implement or evaluate ORTHRUS, CamFlow or the other PIDS examined by Bilot et al. (2025). They also do not establish improvements in intrusion-detection accuracy, analyst investigation time or robustness under telemetry loss.

As the home-laboratory configuration develops, this document will be updated with results from additional controlled experiments. The next revision should explicitly connect the evaluation measures used in the literature with those implemented in the proposed comparative study.

## References

Bilot, T., Jiang, B., Li, Z., El Madhoun, N., Al Agha, K., Zouaoui, A., & Pasquier, T. (2025). Sometimes simpler is better: A comprehensive analysis of state-of-the-art provenance-based intrusion detection systems. In *Proceedings of the 34th USENIX Security Symposium* (pp. 7193–7212). USENIX Association. https://www.usenix.org/conference/usenixsecurity25/presentation/bilot

Jiang, B., Bilot, T., El Madhoun, N., Al Agha, K., Zouaoui, A., Iqbal, S., Han, X., & Pasquier, T. (2025). ORTHRUS: Achieving high quality of attribution in provenance-based intrusion detection systems. In *Proceedings of the 34th USENIX Security Symposium* (pp. 7173–7192). USENIX Association. https://www.usenix.org/conference/usenixsecurity25/presentation/jiang-baoxiang

Pasquier, T., Han, X., Goldstein, M., Moyer, T., Eyers, D., Seltzer, M., & Bacon, J. (2017). Practical whole-system provenance capture. In *Proceedings of the 2017 Symposium on Cloud Computing* (pp. 405–418). Association for Computing Machinery. https://doi.org/10.1145/3127479.3129249
