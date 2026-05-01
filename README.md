# Quantum Cybersecurity Lab

Educational notes, experiments, and practical references on quantum computing applied to cybersecurity, cryptography, and post-quantum security.

## Purpose

This repository documents a practical learning path on quantum computing with a cybersecurity-oriented perspective.

The goal is not to build a physical quantum computer, but to understand how quantum computing works, how quantum algorithms are executed, and what their long-term implications are for classical cryptography and cybersecurity.

## Topics

- Quantum computing fundamentals
- Qubits, gates, circuits, and measurement
- IBM Quantum and Qiskit experiments
- Quantum simulators
- Grover's algorithm
- Shor's algorithm on toy examples
- Quantum Key Distribution
- Post-Quantum Cryptography
- Security implications of quantum computing

## Repository Structure

```text
quantum-cybersecurity-lab/
├── notebooks/
│   ├── 01_quantum_basics.md
│   ├── 02_qubits_and_gates.md
│   ├── 03_bell_states.md
│   ├── 04_grovers_algorithm.md
│   ├── 05_shors_algorithm_toy_example.md
│   └── 06_quantum_key_distribution_bb84.md
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
│   ├── quantum_for_cybersecurity.md
│   ├── post_quantum_crypto.md
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

## Learning Roadmap

1. Quantum computing basics
2. Qubits and quantum gates
3. Bell states and entanglement
4. Grover's algorithm
5. Shor's algorithm on toy examples
6. Quantum Key Distribution and BB84
7. Post-Quantum Cryptography
8. IBM Quantum experiments

See also: [`ROADMAP.md`](ROADMAP.md).

## Cybersecurity Positioning

This repository connects quantum computing fundamentals with cybersecurity-relevant questions:

- What happens to RSA and ECC in a post-quantum world?
- How does Grover's algorithm affect brute-force security margins?
- What is the difference between QKD and PQC?
- How should organizations think about quantum migration?
- What does `harvest now, decrypt later` mean for long-term confidentiality?

## Current Executable Experiments

- Basic single-qubit circuits
- Hadamard superposition demo
- Phase demo
- Bell-state circuits
- Toy Grover search over a two-qubit space

## Status

Work in progress.
