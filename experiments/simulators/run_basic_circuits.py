"""
Run basic quantum circuits on a local Qiskit Aer simulator.

Usage:
    python experiments/simulators/run_basic_circuits.py
"""

from src.circuits.basic_circuits import (
    single_qubit_zero_measurement,
    single_qubit_x_gate,
    single_qubit_hadamard,
    single_qubit_phase_demo,
)
from src.circuits.simulator_utils import print_counts


EXPERIMENTS = {
    "Single qubit initialized in |0>": single_qubit_zero_measurement,
    "Single qubit with X gate": single_qubit_x_gate,
    "Single qubit with Hadamard gate": single_qubit_hadamard,
    "Single qubit phase demo": single_qubit_phase_demo,
}


def main() -> None:
    """Execute all basic circuit experiments."""
    for title, builder in EXPERIMENTS.items():
        print("=" * 72)
        print(title)
        print("=" * 72)
        circuit = builder()
        print(circuit)
        print("Measurement counts:")
        print_counts(circuit, shots=1024)
        print()


if __name__ == "__main__":
    main()
