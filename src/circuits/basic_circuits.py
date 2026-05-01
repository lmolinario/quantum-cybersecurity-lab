"""
Basic quantum circuits used throughout the Quantum Cybersecurity Lab.

This module contains simple, reusable Qiskit circuit builders.
The functions are intentionally minimal and educational.
"""

from qiskit import QuantumCircuit


def single_qubit_zero_measurement() -> QuantumCircuit:
    """Create a circuit that measures a single qubit initialized in |0>."""
    circuit = QuantumCircuit(1, 1)
    circuit.measure(0, 0)
    return circuit


def single_qubit_x_gate() -> QuantumCircuit:
    """Create a circuit that applies an X gate and then measures the qubit."""
    circuit = QuantumCircuit(1, 1)
    circuit.x(0)
    circuit.measure(0, 0)
    return circuit


def single_qubit_hadamard() -> QuantumCircuit:
    """Create a circuit that applies a Hadamard gate and then measures the qubit."""
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    return circuit


def single_qubit_phase_demo() -> QuantumCircuit:
    """Create a simple circuit showing how phase gates can affect later measurements."""
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.z(0)
    circuit.h(0)
    circuit.measure(0, 0)
    return circuit
