# Post-Quantum Cryptography

Post-Quantum Cryptography (PQC) studies cryptographic algorithms designed to remain secure against both classical and quantum adversaries while running on classical computers.

## 1. Why PQC Matters

Quantum computing may eventually threaten widely deployed public-key cryptography.

The most important risk is related to Shor's algorithm, which can theoretically break cryptosystems based on integer factorization and discrete logarithms.

Affected families include:

- RSA
- finite-field Diffie-Hellman
- elliptic-curve Diffie-Hellman
- DSA/ECDSA and other classical public-key signature schemes

The practical message is simple: organizations should not wait for a cryptographically relevant quantum computer before starting the migration inventory.

## 2. Harvest Now, Decrypt Later

A central concern is the `harvest now, decrypt later` threat model.

In this model, an adversary collects encrypted data today and stores it until future quantum capabilities make decryption possible.

This is especially relevant for data with long-term confidentiality requirements, such as:

- government records;
- legal and evidentiary archives;
- intelligence or investigative material;
- health records;
- trade secrets;
- long-lived credentials and key-encryption material.

## 3. PQC vs QKD

Post-Quantum Cryptography and Quantum Key Distribution are different approaches.

PQC:

- runs on classical computers;
- can be integrated into existing protocols;
- is software-deployable;
- is relevant to broad migration strategies;
- is the main practical path for most organizations.

QKD:

- uses quantum communication channels;
- requires specialized infrastructure;
- is mostly relevant to specific high-security communication scenarios;
- does not replace the broader need for PQC in signatures, certificates, software distribution, identity, and ordinary internet protocols.

## 4. Current Standardization Baseline

The main operational baseline is the NIST post-quantum standardization process.

As of the first finalized NIST standards:

| Standard | Algorithm name | Original family/name | Main use |
|---|---|---|---|
| FIPS 203 | ML-KEM | CRYSTALS-Kyber | Key encapsulation and general encryption workflows |
| FIPS 204 | ML-DSA | CRYSTALS-Dilithium | Digital signatures |
| FIPS 205 | SLH-DSA | SPHINCS+ | Stateless hash-based digital signatures and backup signature diversity |

The migration path should be based on standardized algorithms, mature implementations, vendor support, and protocol-level interoperability rather than custom cryptographic design.

## 5. Main PQC Families

Common families of post-quantum algorithms include:

- lattice-based cryptography;
- code-based cryptography;
- hash-based signatures;
- multivariate cryptography;
- zero-knowledge and MPC-in-the-head approaches;
- isogeny-based approaches, although some proposals have been broken or weakened.

Each family has different trade-offs in key size, signature size, ciphertext size, performance, maturity, and implementation risk.

## 6. Migration Challenges

PQC migration is not only a mathematical problem.

It also involves:

- asset inventory;
- cryptographic inventory;
- protocol compatibility;
- performance testing;
- certificate management;
- hardware security module support;
- interoperability;
- compliance;
- vendor readiness;
- long-term data protection;
- evidence and signature preservation.

## 7. Cybersecurity Management Perspective

From a security management perspective, PQC should be treated as a migration program.

Important steps include:

```text
1. Identify cryptographic assets.
2. Identify long-term confidentiality and verifiability needs.
3. Prioritize systems exposed to harvest-now-decrypt-later risk.
4. Map certificates, keys, protocols, and vendors.
5. Test post-quantum or hybrid alternatives.
6. Plan staged deployments.
7. Monitor standards, vendor support, and national/european guidance.
```

See also: [`quantum_safe_readiness.md`](quantum_safe_readiness.md).

## 8. Key Takeaways

- PQC is a practical response to future quantum threats.
- The main concern is classical public-key cryptography.
- Symmetric cryptography is affected differently: Grover's algorithm mainly reduces brute-force margins, so adequate key sizes remain central.
- Migration requires governance, inventory, testing, interoperability, and vendor coordination.
- PQC is highly relevant to cybersecurity strategy, public-sector systems, and digital-forensics evidence preservation.

## References

- NIST, *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*, 2024.
- NIST, *FIPS 204: Module-Lattice-Based Digital Signature Standard*, 2024.
- NIST, *FIPS 205: Stateless Hash-Based Digital Signature Standard*, 2024.
- European Commission, *A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography*, 2025.
