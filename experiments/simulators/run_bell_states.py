"""
Run Bell-state circuits on a local Qiskit Aer simulator.

Usage:
    python experiments/simulators/run_bell_states.py
"""

from src.circuits.bell_states import (
    bell_phi_plus,
    bell_phi_minus,
    bell_psi_plus,
    bell_psi_minus,
)
from src.circuits.simulator_utils import print_counts


EXPERIMENTS = {
    "Bell Phi Plus": bell_phi_plus,
    "Bell Phi Minus": bell_phi_minus,
    "Bell Psi Plus": bell_psi_plus,
    "Bell Psi Minus": bell_psi_minus,
}


def main() -> None:
    """Execute all Bell-state experiments."""
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
