# Related work and questions for the proposal

These are working reading notes for my undergraduate project, not a finished literature review. The full thematic review is being revised separately. I have kept this list short so that each source can be checked against its full text before I make detailed claims about results.

## Papers to examine closely

### ORTHRUS: Achieving High Quality of Attribution in Provenance-based Intrusion Detection Systems (USENIX Security, 2025)

The issue I want to examine is the distinction between detecting suspicious activity and attributing the relevant activity to an attack. My proposed comparison should therefore evaluate the reconstructed attack chain, not just count alerts. I still need to check the paper's evaluation protocol and determine which of its attribution measures are appropriate for my smaller lab.

### Sometimes Simpler is Better: A Comprehensive Analysis of State-of-the-Art Provenance-Based Intrusion Detection Systems (USENIX Security, 2025)

This is important to my proposed lightweight approach. I need to understand what the authors actually found about complexity, baselines, and practical PIDS evaluation before treating simplicity as an advantage. The experiment should compare analytical approaches fairly rather than assume that a smaller system is better.

### CamFlow: Managed Data-sharing for Cloud Services (provenance collection literature)

I want to understand what information a dedicated provenance collector captures that is missing from my current Linux Audit and SOC event records. This matters because a graph assembled from selected audit events cannot be assumed to have the completeness or semantics of system-level provenance. I need to verify the precise CamFlow publication and citation before including it in the formal bibliography.

## Questions arising from the reading

1. What constitutes a valid causal edge, and what evidence is needed beyond temporal proximity?
2. Which attribution-quality metrics can be measured without recruiting a large analyst cohort?
3. How can configurations A, B and C be compared without confusing extra sensor coverage with improved analysis?
4. Which event-loss mechanisms are realistic, and how should repeated loss trials be sampled?
5. Would a dedicated provenance collector provide a useful reference condition for judging what ordinary SOC telemetry cannot reconstruct?

## Boundary of the present evidence

My published Experiments 03 and 04 are controlled Linux Audit reconstructions. They do not evaluate ORTHRUS, CamFlow, or any other published PIDS implementation. They do not yet support a claim about intrusion-detection accuracy or improved analyst performance.

The next revision of this note should add verified bibliographic details, specific passages or results from the papers, and a comparison of experimental assumptions. I will not present a publication as fully reviewed until I have checked its full text.
