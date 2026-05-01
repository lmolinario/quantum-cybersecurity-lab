# 02 - Qubits and Quantum Gates

This note introduces the most important elementary quantum gates used in simple quantum circuits.

## 1. Qubits

A qubit is the basic unit of quantum information.

Unlike a classical bit, which can only be `0` or `1`, a qubit can exist in a quantum state that allows probabilistic measurement outcomes.

A qubit is usually represented using the basis states:

```text
|0>
|1>
```

## 2. Quantum Gates

Quantum gates modify the state of one or more qubits.

They are the quantum equivalent of logical operations, but they behave differently from classical logic gates because they operate on quantum states.

## 3. X Gate

The X gate is similar to a classical NOT gate.

It transforms:

```text
|0> -> |1>
|1> -> |0>
```

Example in Qiskit:

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.x(0)
qc.measure(0, 0)

qc.draw("mpl")
```

## 4. Hadamard Gate

The Hadamard gate creates superposition.

Starting from `|0>`, it produces a state that has approximately equal probability of being measured as `0` or `1`.

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

qc.draw("mpl")
```

## 5. Z Gate

The Z gate changes the phase of the `|1>` component of a qubit.

This is important because quantum computation is not only about probabilities, but also about phase and interference.

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(1, 1)
qc.h(0)
qc.z(0)
qc.h(0)
qc.measure(0, 0)

qc.draw("mpl")
```

## 6. CNOT Gate

The CNOT gate operates on two qubits:

- one control qubit
- one target qubit

If the control qubit is `1`, the target qubit is flipped.

```python
from qiskit import QuantumCircuit

qc = QuantumCircuit(2, 2)
qc.x(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

qc.draw("mpl")
```

## 7. Measurement

Measurement converts quantum information into classical information.

After measurement, a qubit produces a classical bit value.

This is why quantum algorithms are designed to manipulate probabilities before measurement.

## 8. Cybersecurity Relevance

Quantum gates are the building blocks of algorithms such as Grover and Shor.

Understanding gates is necessary before studying the impact of quantum computing on cryptography.

## Key Takeaways

- Quantum gates operate on qubits.
- X behaves like a bit flip.
- H creates superposition.
- Z affects quantum phase.
- CNOT enables multi-qubit operations.
- Measurement produces classical output.
