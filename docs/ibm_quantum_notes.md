# IBM Quantum Notes

This document collects operational notes for using IBM Quantum and Qiskit.

## 1. Purpose

IBM Quantum allows users to design, simulate, and execute quantum circuits using Qiskit and IBM quantum backends.

For this repository, IBM Quantum is used as a learning and experimentation platform.

## 2. Local Simulation vs Real Hardware

Quantum circuits can be executed in two main ways:

- local or cloud simulators
- real quantum hardware backends

Simulators are useful for learning and debugging.

Real hardware introduces noise, decoherence, gate errors, and queue times.

## 3. Typical Workflow

```text
1. Create a quantum circuit in Qiskit
2. Test it with a simulator
3. Inspect expected measurement counts
4. Select an IBM Quantum backend
5. Execute the circuit on real hardware
6. Compare simulator and hardware results
7. Analyze noise and deviations
```

## 4. Why Results Differ on Real Hardware

Real quantum computers are noisy.

Possible sources of error include:

- imperfect gates
- decoherence
- readout errors
- limited connectivity
- calibration variability

This means that real hardware results may differ from ideal simulation results.

## 5. Educational Value

Running small circuits on real quantum hardware is useful because it shows the difference between theoretical quantum circuits and physical quantum devices.

This is important for understanding why practical quantum computing requires error correction and robust hardware.

## 6. Security Relevance

For cybersecurity, IBM Quantum can be used to study toy versions of quantum algorithms and understand their conceptual implications.

However, educational experiments on current devices must not be confused with practical cryptographic attacks.

## Key Takeaways

- IBM Quantum is useful for education and experimentation.
- Simulators and hardware backends behave differently.
- Noise is a central limitation of current quantum devices.
- Toy demonstrations are useful for learning, not for breaking real systems.
