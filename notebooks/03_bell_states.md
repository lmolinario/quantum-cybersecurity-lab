# 03 - Bell States and Entanglement

This note introduces Bell states, which are among the simplest and most important examples of quantum entanglement.

## 1. What Is Entanglement?

Entanglement is a quantum phenomenon where the state of two or more qubits cannot be fully described independently.

When two qubits are entangled, measuring one qubit gives information about the other, even if they are physically separated.

This does not allow faster-than-light communication, but it is one of the core resources used in quantum computing and quantum information.

## 2. Creating a Bell State

A simple Bell state can be created using:

1. a Hadamard gate on the first qubit
2. a CNOT gate between the first and second qubit

Conceptual circuit:

```text
q0: |0> ── H ──■── Measure
               │
q1: |0> ───────X── Measure
```

## 3. Qiskit Example

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

simulator = AerSimulator()
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

print(counts)
```

Expected output:

```text
{'00': about 512, '11': about 512}
```

The exact numbers vary because measurement is probabilistic.

## 4. Interpretation

The result should mostly contain only:

```text
00
11
```

This means that the two qubits are correlated.

If the first qubit is measured as `0`, the second is also measured as `0`.

If the first qubit is measured as `1`, the second is also measured as `1`.

## 5. Why This Matters

Entanglement is a fundamental resource for:

- quantum algorithms
- quantum communication
- quantum teleportation
- quantum key distribution
- quantum error correction

## 6. Cybersecurity Relevance

Entanglement is relevant to cybersecurity because it appears in quantum communication and quantum key distribution protocols.

While most practical cybersecurity threats from quantum computing are currently related to cryptography and future quantum algorithms, entanglement is one of the physical and computational principles that makes quantum information different from classical information.

## Key Takeaways

- A Bell state is a simple entangled two-qubit state.
- Hadamard plus CNOT can create entanglement.
- Measurement results are correlated.
- Entanglement is central to quantum computing and quantum communication.
