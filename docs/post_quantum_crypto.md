# Post-Quantum Cryptography

Post-Quantum Cryptography (PQC) studies cryptographic algorithms designed to remain secure against both classical and quantum adversaries.

## 1. Why PQC Matters

Quantum computing may eventually threaten widely deployed public-key cryptography.

The most important risk is related to algorithms such as Shor's algorithm, which can theoretically break cryptosystems based on integer factorization and discrete logarithms.

Affected families include:

- RSA
- Diffie-Hellman
- Elliptic Curve Cryptography
- many classical digital signature schemes

## 2. Harvest Now, Decrypt Later

A central concern is the `harvest now, decrypt later` threat model.

In this model, an adversary collects encrypted data today and stores it until future quantum capabilities make decryption possible.

This is especially relevant for data with long-term confidentiality requirements.

## 3. PQC vs QKD

Post-Quantum Cryptography and Quantum Key Distribution are different approaches.

PQC:

- runs on classical computers
- can be integrated into existing protocols
- is software-deployable
- is relevant to broad migration strategies

QKD:

- uses quantum communication channels
- requires specialized infrastructure
- is mostly relevant to specific high-security communication scenarios

## 4. Main PQC Families

Common families of post-quantum algorithms include:

- lattice-based cryptography
- code-based cryptography
- hash-based signatures
- multivariate cryptography
- isogeny-based approaches, although some proposals have been broken or weakened

## 5. Migration Challenges

PQC migration is not only a mathematical problem.

It also involves:

- asset inventory
- cryptographic inventory
- protocol compatibility
- performance testing
- certificate management
- interoperability
- compliance
- long-term data protection

## 6. Cybersecurity Management Perspective

From a security management perspective, PQC should be treated as a migration program.

Important steps include:

```text
1. Identify cryptographic assets
2. Identify long-term confidentiality needs
3. Prioritize systems exposed to harvest-now-decrypt-later risk
4. Test post-quantum alternatives
5. Plan hybrid deployments
6. Monitor standards and vendor support
```

## 7. Key Takeaways

- PQC is a practical response to future quantum threats.
- The main concern is public-key cryptography.
- Migration will require governance, inventory, and testing.
- PQC is highly relevant to cybersecurity strategy.
