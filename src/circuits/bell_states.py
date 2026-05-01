"""
Bell-state circuit builders.

Bell states are among the simplest examples of quantum entanglement.

Note:
    When measured only in the computational basis, Bell states that differ
    only by a relative phase can produce the same measurement counts.
    Distinguishing phase differences requires additional basis changes or
    statevector-level analysis.
"""

from qiskit import QuantumCircuit


def bell_phi_plus() -> QuantumCircuit:
    """Create the Bell state |Phi+> = (|00> + |11>) / sqrt(2)."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def bell_phi_minus() -> QuantumCircuit:
    """Create the Bell state |Phi-> = (|00> - |11>) / sqrt(2)."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.z(0)
    circuit.measure([0, 1], [0, 1])
    return circuit


def bell_psi_plus() -> QuantumCircuit:
    """Create the Bell state |Psi+> = (|01> + |10>) / sqrt(2)."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.x(1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def bell_psi_minus() -> QuantumCircuit:
    """Create the Bell state |Psi-> = (|01> - |10>) / sqrt(2)."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.x(1)
    circuit.z(0)
    circuit.measure([0, 1], [0, 1])
    return circuit
