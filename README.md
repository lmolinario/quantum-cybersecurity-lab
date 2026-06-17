# Quantum Cybersecurity Lab

[![Python CI](https://github.com/lmolinario/quantum-cybersecurity-lab/actions/workflows/python-ci.yml/badge.svg)](https://github.com/lmolinario/quantum-cybersecurity-lab/actions/workflows/python-ci.yml)

Educational notes, executable notebooks, experiments, and practical references on quantum computing applied to cybersecurity, cryptography, post-quantum security, and quantum-safe readiness.

## Purpose

This repository documents a practical learning path on quantum computing with a cybersecurity-oriented perspective.

The goal is not to build a physical quantum computer, but to understand how quantum computing works, how quantum algorithms are executed, and what their long-term implications are for classical cryptography, cybersecurity governance, and post-quantum migration planning.

## Topics

- Quantum computing fundamentals
- Qubits, gates, circuits, and measurement
- IBM Quantum and Qiskit experiments
- Quantum simulators
- Grover's algorithm
- Shor's algorithm on toy examples
- Quantum Key Distribution
- Post-Quantum Cryptography
- Quantum-safe readiness assessment
- Cryptographic inventory and migration planning
- Security implications of quantum computing

## Open in Google Colab

Run the notebooks directly in Google Colab without cloning the repository.

| # | Notebook | Open in Colab |
|---|---|---|
| 01 | Quantum Computing Basics | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/01_quantum_basics.ipynb) |
| 02 | Qubits and Quantum Gates | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/02_qubits_and_gates.ipynb) |
| 03 | Bell States and Entanglement | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/03_bell_states.ipynb) |
| 04 | Grover's Algorithm | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/04_grovers_algorithm.ipynb) |
| 05 | Shor's Algorithm Toy Example | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/05_shors_algorithm_toy_example.ipynb) |
| 06 | Quantum Key Distribution and BB84 | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/06_quantum_key_distribution_bb84.ipynb) |
| 07 | Post-Quantum Cryptography | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/07_post_quantum_cryptography.ipynb) |

More details: [`docs/colab.md`](docs/colab.md).

## Repository Structure

```text
quantum-cybersecurity-lab/
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── notebooks/
│   ├── 01_quantum_basics.md
│   ├── 01_quantum_basics.ipynb
│   ├── 02_qubits_and_gates.md
│   ├── 02_qubits_and_gates.ipynb
│   ├── 03_bell_states.md
│   ├── 03_bell_states.ipynb
│   ├── 04_grovers_algorithm.md
│   ├── 04_grovers_algorithm.ipynb
│   ├── 05_shors_algorithm_toy_example.md
│   ├── 05_shors_algorithm_toy_example.ipynb
│   ├── 06_quantum_key_distribution_bb84.md
│   ├── 06_quantum_key_distribution_bb84.ipynb
│   └── 07_post_quantum_cryptography.ipynb
│
├── src/
│   ├── circuits/
│   │   ├── basic_circuits.py
│   │   ├── bell_states.py
│   │   └── simulator_utils.py
│   ├── algorithms/
│   │   └── grover_toy.py
│   └── crypto/
│
├── docs/
│   ├── setup.md
│   ├── colab.md
│   ├── quantum_for_cybersecurity.md
│   ├── post_quantum_crypto.md
│   ├── quantum_safe_readiness.md
│   ├── ibm_quantum_notes.md
│   └── security_impact_matrix.md
│
├── experiments/
│   ├── ibm_quantum/
│   └── simulators/
│       ├── run_basic_circuits.py
│       ├── run_bell_states.py
│       └── run_grover_toy.py
│
├── scripts/
│   ├── validate_notebooks.py
│   └── crypto_inventory.py
├── references/
│   └── bibliography.bib
├── ROADMAP.md
└── requirements.txt
```

## Quick Start

```bash
git clone https://github.com/lmolinario/quantum-cybersecurity-lab.git
cd quantum-cybersecurity-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run local simulator experiments:

```bash
python experiments/simulators/run_basic_circuits.py
python experiments/simulators/run_bell_states.py
python experiments/simulators/run_grover_toy.py
```

Run the quantum-safe inventory helper:

```bash
python scripts/crypto_inventory.py --path . --format json
python scripts/crypto_inventory.py --tls-endpoint example.com:443 --format json
```

Validate notebooks:

```bash
python scripts/validate_notebooks.py
```

Open Jupyter:

```bash
jupyter notebook
```

## Executable Notebooks

1. `01_quantum_basics.ipynb`
2. `02_qubits_and_gates.ipynb`
3. `03_bell_states.ipynb`
4. `04_grovers_algorithm.ipynb`
5. `05_shors_algorithm_toy_example.ipynb`
6. `06_quantum_key_distribution_bb84.ipynb`
7. `07_post_quantum_cryptography.ipynb`

## Continuous Integration

A GitHub Actions workflow validates the notebooks, compiles the inventory helper, and runs the simulator experiments automatically on pushes and pull requests to `main`.

Workflow file:

```text
.github/workflows/python-ci.yml
```

## Learning Roadmap

1. Quantum computing basics
2. Qubits and quantum gates
3. Bell states and entanglement
4. Grover's algorithm
5. Shor's algorithm on toy examples
6. Quantum Key Distribution and BB84
7. Post-Quantum Cryptography
8. Quantum-safe readiness assessment
9. IBM Quantum experiments

See also: [`ROADMAP.md`](ROADMAP.md).

## Cybersecurity Positioning

This repository connects quantum computing fundamentals with cybersecurity-relevant questions:

- What happens to RSA and ECC in a post-quantum world?
- How does Grover's algorithm affect brute-force security margins?
- What is the difference between QKD and PQC?
- How should organizations think about quantum migration?
- What does `harvest now, decrypt later` mean for long-term confidentiality?
- How can a cryptographic inventory support a quantum-safe transition program?

## Quantum-Safe Readiness

The repository now includes a governance-oriented readiness layer:

- [`docs/quantum_safe_readiness.md`](docs/quantum_safe_readiness.md) defines a practical assessment workflow.
- [`scripts/crypto_inventory.py`](scripts/crypto_inventory.py) performs a lightweight first-pass scan for cryptographic files, key material indicators, and TLS endpoint metadata.
- [`docs/security_impact_matrix.md`](docs/security_impact_matrix.md) summarizes the operational impact of quantum computing on cryptographic controls.

This layer is intended for learning, portfolio demonstration, and early-stage risk assessment. It does not replace a formal cryptographic audit.

## Current Executable Experiments

- Basic single-qubit circuits
- Hadamard superposition demo
- Phase demo
- Bell-state circuits
- Toy Grover search over a two-qubit space
- Notebook JSON validation
- Lightweight cryptographic inventory helper

## Status

Work in progress.
