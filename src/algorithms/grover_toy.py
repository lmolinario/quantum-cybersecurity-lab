"""
Toy Grover-style circuit builder.

This is an educational implementation for a two-qubit search space.
It is not intended for cryptanalytic use.
"""

from qiskit import QuantumCircuit


def grover_search_11() -> QuantumCircuit:
    """
    Build a simple two-qubit Grover circuit that marks the target state |11>.

    The circuit uses:
    - Hadamard gates to create superposition
    - a controlled-Z-style oracle for |11>
    - a diffusion step
    - final measurement
    """
    circuit = QuantumCircuit(2, 2)

    # Create uniform superposition.
    circuit.h([0, 1])

    # Oracle for target state |11>.
    circuit.cz(0, 1)

    # Diffusion operator for two qubits.
    circuit.h([0, 1])
    circuit.x([0, 1])
    circuit.h(1)
    circuit.cx(0, 1)
    circuit.h(1)
    circuit.x([0, 1])
    circuit.h([0, 1])

    circuit.measure([0, 1], [0, 1])
    return circuit
