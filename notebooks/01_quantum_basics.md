# 01 - Quantum Computing Basics

This note introduces the basic concepts of quantum computing with a cybersecurity-oriented perspective.

## 1. Classical Bit vs Qubit

A classical bit can be either `0` or `1`.

A qubit can be in a quantum state that combines the possibilities of `0` and `1` until it is measured.

When measured, the qubit collapses to a classical value: either `0` or `1`.

## 2. Basic Quantum Circuit

A quantum circuit is composed of:

- qubits
- quantum gates
- measurements
- classical output bits

Example conceptual circuit:

```text
|0> ── H ── Measure
