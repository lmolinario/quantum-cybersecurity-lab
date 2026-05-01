# Open in Google Colab

This page provides direct Google Colab links for the executable notebooks in this repository.

## Notebooks

| # | Notebook | Open in Colab |
|---|---|---|
| 01 | Quantum Computing Basics | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/01_quantum_basics.ipynb) |
| 02 | Qubits and Quantum Gates | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/02_qubits_and_gates.ipynb) |
| 03 | Bell States and Entanglement | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/03_bell_states.ipynb) |
| 04 | Grover's Algorithm | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/04_grovers_algorithm.ipynb) |
| 05 | Shor's Algorithm Toy Example | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/05_shors_algorithm_toy_example.ipynb) |
| 06 | Quantum Key Distribution and BB84 | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/06_quantum_key_distribution_bb84.ipynb) |
| 07 | Post-Quantum Cryptography | [Open](https://colab.research.google.com/github/lmolinario/quantum-cybersecurity-lab/blob/main/notebooks/07_post_quantum_cryptography.ipynb) |

## Colab Runtime Notes

Google Colab does not always include Qiskit by default.

If a notebook fails with `ModuleNotFoundError`, run this cell first:

```python
!pip install -q qiskit qiskit-aer
```

For the Post-Quantum Cryptography notebook, `pandas` is usually already available in Colab. If needed, run:

```python
!pip install -q pandas
```

## Recommended Use

Use Colab for quick interactive exploration.

Use the local setup described in `docs/setup.md` for reproducible local experiments and development.
