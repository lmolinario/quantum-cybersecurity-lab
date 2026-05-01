"""
Utility functions for running Qiskit circuits on local simulators.
"""

from __future__ import annotations

from typing import Dict

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def run_counts(circuit: QuantumCircuit, shots: int = 1024) -> Dict[str, int]:
    """
    Execute a quantum circuit on the Aer simulator and return measurement counts.

    Args:
        circuit: Qiskit quantum circuit with measurements.
        shots: Number of repeated executions.

    Returns:
        Dictionary mapping measured bitstrings to counts.
    """
    simulator = AerSimulator()
    result = simulator.run(circuit, shots=shots).result()
    return result.get_counts()


def print_counts(circuit: QuantumCircuit, shots: int = 1024) -> None:
    """Run a circuit and print measurement counts."""
    counts = run_counts(circuit, shots=shots)
    for state, count in sorted(counts.items()):
        print(f"{state}: {count}")
