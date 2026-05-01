# 05 - Shor's Algorithm Toy Example

This note introduces Shor's algorithm at a conceptual level and explains why it matters for cybersecurity.

## 1. What Problem Does Shor's Algorithm Solve?

Shor's algorithm is a quantum algorithm for integer factorization and discrete logarithms.

These problems are important because widely used public-key cryptographic systems rely on their classical hardness.

Examples:

- RSA relies on the difficulty of factoring large integers.
- ECC relies on the difficulty of the elliptic curve discrete logarithm problem.

## 2. Cybersecurity Relevance

A sufficiently large, fault-tolerant quantum computer running Shor's algorithm could threaten:

- RSA
- Diffie-Hellman
- Elliptic Curve Cryptography
- many digital signature schemes based on number theory

This is one of the main reasons behind the development of Post-Quantum Cryptography.

## 3. Toy Factorization Example

A common educational example is factoring a small number such as:

```text
15 = 3 x 5
```

This is trivial classically, but it is useful to understand the structure of the algorithm.

The purpose of a toy example is not to demonstrate practical cryptanalytic power.

The purpose is to show how a quantum circuit can be used as part of a factorization procedure.

## 4. High-Level Structure of Shor's Algorithm

Shor's algorithm combines classical and quantum steps.

```text
1. Choose a number N to factor
2. Select a random integer a < N
3. Check whether gcd(a, N) already gives a factor
4. Use a quantum period-finding subroutine
5. Use the discovered period to compute non-trivial factors of N
```

The quantum part is mainly used for period finding.

## 5. Why Period Finding Matters

The key insight is that factorization can be reduced to finding the period of a modular exponential function.

Quantum computers can estimate this period efficiently using quantum phase estimation and the quantum Fourier transform.

## 6. Important Limitation

Small demonstrations of Shor's algorithm do not mean that current quantum computers can break real RSA or ECC keys.

Breaking real-world cryptographic keys would require large, reliable, error-corrected quantum computers.

Current educational demonstrations are useful for learning, not for practical attacks.

## 7. Post-Quantum Security Lesson

Organizations should not wait for practical quantum attacks before planning migration.

The relevant risk model is often called:

```text
Harvest now, decrypt later
```

An attacker may collect encrypted data today and decrypt it in the future if quantum capabilities become available.

## 8. Key Takeaways

- Shor's algorithm threatens RSA and ECC in principle.
- The quantum core of the algorithm is period finding.
- Toy examples are educational, not operationally dangerous.
- Real cryptographic impact requires fault-tolerant quantum computers.
- Shor's algorithm motivates post-quantum migration.
