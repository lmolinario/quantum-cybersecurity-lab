# Quantum Security Impact Matrix

This matrix summarizes the main cybersecurity implications of quantum computing.

| Area | Quantum Relevance | Main Risk | Practical Response |
|---|---|---|---|
| RSA | Shor's algorithm | Future factorization of large moduli | Plan PQC migration |
| ECC | Shor's algorithm | Future discrete logarithm attacks | Plan PQC migration |
| Diffie-Hellman | Shor's algorithm | Future key exchange compromise | Use PQC or hybrid key exchange |
| Symmetric encryption | Grover's algorithm | Reduced brute-force margin | Prefer larger key sizes, e.g. 256-bit |
| Hash preimage resistance | Grover's algorithm | Quadratic search speedup | Use adequate hash output sizes |
| Digital signatures | Shor's algorithm | Future signature forgery risk | Move to PQC signatures |
| Long-term confidential data | Harvest now, decrypt later | Future decryption of collected data | Prioritize migration for sensitive archives |
| Secure communications | QKD/PQC | Need for future-proof key establishment | Evaluate PQC first; QKD for special contexts |
| Digital forensics | Long-term evidence integrity | Signature and encryption durability | Future-proof evidence preservation workflows |

## Interpretation

Quantum computing should be treated as a strategic cybersecurity risk.

The most urgent planning area is not immediate attack capability, but migration readiness for systems and data with long-term confidentiality or integrity requirements.

## Key Message

Post-quantum readiness is a governance, architecture, and inventory problem before it becomes a deployment problem.
