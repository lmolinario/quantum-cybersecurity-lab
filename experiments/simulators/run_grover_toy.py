"""
Run a toy Grover search circuit on a local Qiskit Aer simulator.

Usage:
    python experiments/simulators/run_grover_toy.py
"""

from src.algorithms.grover_toy import grover_search_11
from src.circuits.simulator_utils import print_counts


def main() -> None:
    """Execute the toy Grover circuit."""
    circuit = grover_search_11()
    print("Toy Grover search for target state |11>")
    print("=" * 72)
    print(circuit)
    print("Measurement counts:")
    print_counts(circuit, shots=1024)


if __name__ == "__main__":
    main()
