# Quantum-Safe Readiness Assessment

This note turns the post-quantum cryptography topic into a practical cybersecurity governance workflow.

The goal is not to replace cryptography directly inside production systems. The first goal is to understand where cryptography is used, which assets depend on quantum-vulnerable public-key algorithms, and which data must remain confidential or verifiable for a long time.

## 1. Threat Model

A sufficiently capable quantum computer would threaten many public-key cryptographic systems currently used for key exchange, encryption, authentication, and digital signatures.

The main risk areas are:

| Area | Classical dependency | Quantum concern | Readiness action |
|---|---|---|---|
| Key exchange | RSA, finite-field DH, ECDH | Shor's algorithm | Inventory protocols and plan PQC or hybrid migration |
| Digital signatures | RSA, DSA, ECDSA, EdDSA | Shor's algorithm | Inventory certificate chains, signing workflows, and timestamping |
| Long-term archives | Public-key protected keys or envelopes | Harvest now, decrypt later | Prioritize data with long confidentiality lifetime |
| TLS/VPN/SSH | Classical authentication and key exchange | Future compromise of public-key components | Track vendor support for PQC and hybrid modes |
| Evidence preservation | Signatures, timestamps, certificate validation | Long-term verifiability risk | Preserve algorithm metadata and migration evidence |
| Symmetric encryption | AES and similar primitives | Grover's algorithm reduces brute-force margin | Prefer adequate security levels, commonly 256-bit where appropriate |

## 2. Practical Scope

A readiness assessment should answer four questions.

1. **Where is cryptography used?**
   - TLS certificates
   - VPN profiles
   - SSH keys
   - code-signing certificates
   - document-signing certificates
   - e-mail encryption/signature workflows
   - database encryption
   - backup encryption
   - digital timestamping
   - forensic evidence preservation workflows

2. **Which algorithms are involved?**
   - RSA
   - finite-field Diffie-Hellman
   - elliptic-curve Diffie-Hellman
   - ECDSA/EdDSA
   - AES key sizes
   - hash functions
   - certificate-chain signature algorithms

3. **How long must the protected information remain secure or verifiable?**
   - days or weeks
   - years
   - decades
   - legal or evidentiary retention period

4. **Who controls the migration path?**
   - internal system owner
   - cloud provider
   - SaaS provider
   - certificate authority
   - software vendor
   - public-sector platform owner

## 3. Readiness Levels

| Level | Description | Expected evidence |
|---|---|---|
| 0 - Unknown | No cryptographic inventory exists | No reliable asset list |
| 1 - Initial inventory | Main certificates, keys, and protocols are listed | Asset table and owner mapping |
| 2 - Risk classified | Assets are mapped to data lifetime and business/legal criticality | Prioritized risk register |
| 3 - Vendor-aware | Third-party dependencies and vendor roadmaps are tracked | Vendor status and renewal constraints |
| 4 - Hybrid testing | PQC or hybrid approaches are tested in non-production environments | Test results and compatibility notes |
| 5 - Migration governed | Transition is managed as a formal architecture and risk program | Roadmap, controls, exceptions, and audit trail |

## 4. Minimum Inventory Schema

Use a simple table before introducing complex tooling.

| Field | Meaning |
|---|---|
| `asset_id` | Unique system, service, or repository identifier |
| `owner` | Technical or organizational owner |
| `environment` | Production, test, development, lab |
| `crypto_use` | TLS, VPN, SSH, signing, storage, backup, evidence preservation |
| `algorithm` | RSA, ECDSA, ECDH, DH, AES-128, AES-256, SHA-256, etc. |
| `key_size_or_curve` | Example: RSA-2048, RSA-3072, P-256, X25519 |
| `certificate_or_key_location` | File path, secret manager, HSM, CA, external provider |
| `data_lifetime` | Expected confidentiality or verifiability lifetime |
| `exposure` | Internet-facing, internal, offline, archived |
| `migration_dependency` | Internal, vendor, cloud provider, CA, unknown |
| `priority` | Low, medium, high, critical |
| `notes` | Constraints, exceptions, renewal windows, test results |

## 5. Suggested Workflow

```text
1. Build a cryptographic asset inventory.
2. Separate public-key, symmetric, hash, and certificate-chain dependencies.
3. Identify data with long-term confidentiality or legal/evidentiary value.
4. Prioritize internet-facing and high-retention systems.
5. Check vendor and platform support for PQC or hybrid modes.
6. Test PQC/hybrid configurations outside production.
7. Document migration blockers, exceptions, and residual risk.
8. Review the inventory periodically as standards, vendors, and protocols evolve.
```

## 6. Using the Inventory Helper

The repository includes a lightweight helper that can identify files and TLS endpoints requiring manual review.

Run a local scan:

```bash
python scripts/crypto_inventory.py --path . --format json
```

Export CSV:

```bash
python scripts/crypto_inventory.py --path . --format csv --output crypto_inventory.csv
```

Inspect public TLS endpoints:

```bash
python scripts/crypto_inventory.py \
  --tls-endpoint example.com:443 \
  --tls-endpoint github.com:443 \
  --format json
```

The helper does **not** certify whether a system is quantum-safe. It only produces a first-pass inventory for governance and technical review.

## 7. Interpretation Rules

- Finding RSA, ECDSA, ECDH, or classical DH does not mean that the system is immediately broken.
- It means that the asset should be included in the post-quantum transition inventory.
- Long-term confidentiality is usually more urgent than short-lived confidentiality because of the `harvest now, decrypt later` scenario.
- Digital signatures and timestamping require special attention because old signatures may need to remain verifiable after classical public-key algorithms become deprecated.
- QKD and PQC are not interchangeable. PQC is software-deployable on classical infrastructure, while QKD requires specialized communication infrastructure and is mainly relevant to specific high-security scenarios.

## 8. Report Template

```text
Quantum-Safe Readiness Mini-Report

Scope:
- Systems reviewed:
- Repositories reviewed:
- TLS endpoints reviewed:
- Date:

Main findings:
- Public-key algorithms detected:
- Certificates or key stores detected:
- Long-term confidentiality assets:
- Evidence or signature workflows:
- Third-party dependencies:

Priority actions:
1.
2.
3.

Open questions:
-
-

Residual risk:
-

Next review date:
-
```

## 9. Reference Positioning

This repository follows a governance-first interpretation of the quantum transition:

- inventory before migration;
- data lifetime before generic urgency;
- hybrid testing before production deployment;
- vendor and protocol support before local custom cryptography;
- evidence preservation as a specific digital-forensics concern.

## References

- Agenzia per la Cybersicurezza Nazionale, *Crittografia Post-Quantum e Quantistica: Preparazione alla Minaccia Quantistica*, July 2024.
- NIST, *FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard*, 2024.
- NIST, *FIPS 204: Module-Lattice-Based Digital Signature Standard*, 2024.
- NIST, *FIPS 205: Stateless Hash-Based Digital Signature Standard*, 2024.
- European Commission, *A Coordinated Implementation Roadmap for the Transition to Post-Quantum Cryptography*, 2025.
