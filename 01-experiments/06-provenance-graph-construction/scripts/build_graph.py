from pathlib import Path
import csv
import json
import re
import hashlib

import networkx as nx
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import os

BASE = Path(__file__).resolve().parents[2]

SOURCE = Path(
    os.environ.get("EXP05_SOURCE", str(BASE / "experiment-05"))
).resolve()

OUT = Path(
    os.environ.get("EXP06_OUTPUT", str(BASE / "experiment-06"))
).resolve()

# Create output directories for reproducible execution
(OUT / "graphs").mkdir(parents=True, exist_ok=True)
(OUT / "results").mkdir(parents=True, exist_ok=True)

run_id = (
    SOURCE / "ubuntu/run-id.txt"
).read_text().strip()

audit_text = "\n".join(
    (SOURCE / f"ubuntu/{name}").read_text()
    for name in ("audit-process.txt", "audit-exec.txt")
)

with (SOURCE / "EXP05-BASELINE-EDGES.csv").open(
    newline=""
) as f:
    rows = list(csv.DictReader(f))

rows = [r for r in rows if r["run_id"] == run_id]

if len(rows) != 2:
    raise SystemExit(
        f"Expected 2 baseline edges; found {len(rows)}"
    )

G = nx.DiGraph()
verified = []

for row in rows:
    parent = int(row["parent_pid"])
    child = int(row["child_pid"])
    syscall = row["creation_syscall"]

    if row["audit_confirmed"] != "1":
        raise SystemExit("Unconfirmed audit edge")

    # Audit process creation records contain:
    # pid=<parent> ... exit=<child>
    matching = [
        line for line in audit_text.splitlines()
        if "type=SYSCALL" in line
        and f"syscall={syscall}" in line
        and re.search(rf"\bpid={parent}\b", line)
        and re.search(rf"\bexit={child}\b", line)
        and "success=yes" in line
    ]

    if not matching:
        raise SystemExit(
            f"Missing raw audit evidence: {parent}->{child}"
        )

    G.add_node(
        parent,
        process=row["parent_process"]
    )
    G.add_node(
        child,
        process=row["child_process"]
    )

    G.add_edge(
        parent,
        child,
        syscall=syscall,
        source="Linux Audit",
        verified=True
    )

    verified.append({
        "parent_pid": parent,
        "child_pid": child,
        "syscall": syscall,
        "audit_records": len(matching)
    })

if not nx.is_directed_acyclic_graph(G):
    raise SystemExit("Unexpected process cycle")

if G.number_of_nodes() != 3 or G.number_of_edges() != 2:
    raise SystemExit("Unexpected graph structure")

graph_path = OUT / "graphs/EXP06-process-provenance.graphml"
png_path = OUT / "graphs/EXP06-process-provenance.png"
json_path = OUT / "results/EXP06-graph-metrics.json"

nx.write_graphml(G, graph_path)

positions = {
    22254: (0, 2),
    22257: (0, 1),
    22258: (0, 0)
}

labels = {
    pid: f"{G.nodes[pid]['process']}\nPID {pid}"
    for pid in G.nodes
}

fig, ax = plt.subplots(figsize=(8, 6))

nx.draw_networkx_nodes(
    G, positions, node_size=4500,
    node_color="#dbeafe", edgecolors="#1e40af",
    ax=ax
)

nx.draw_networkx_labels(
    G, positions, labels=labels,
    font_size=11, ax=ax
)

nx.draw_networkx_edges(
    G, positions, arrows=True,
    arrowsize=22, node_size=4500,
    width=2, edge_color="#2563eb", ax=ax
)

nx.draw_networkx_edge_labels(
    G, positions,
    edge_labels=nx.get_edge_attributes(G, "syscall"),
    font_size=10, ax=ax
)

ax.set_title(
    "Experiment 06: Linux Audit Process Provenance"
)
ax.axis("off")
fig.tight_layout()
fig.savefig(png_path, dpi=180)
plt.close(fig)

metrics = {
    "experiment": "06",
    "source_experiment": "05",
    "run_id": run_id,
    "nodes": G.number_of_nodes(),
    "edges": G.number_of_edges(),
    "directed_acyclic": nx.is_directed_acyclic_graph(G),
    "verified_audit_edges": verified,
    "scope": "single controlled process chain"
}

json_path.write_text(json.dumps(metrics, indent=2) + "\n")

for path in (graph_path, png_path, json_path):
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"{path.name}: {digest}")

print(json.dumps(metrics, indent=2))
print("EXP06_GRAPH_CONSTRUCTION_COMPLETE")
