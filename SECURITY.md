# Security Policy

## Supported versions

This repository is an educational project under active development. Security fixes are applied to the current `main` branch; older snapshots and forks are not maintained.

## Reporting a vulnerability

Do not disclose suspected vulnerabilities, exposed secrets, or sensitive cryptographic material in a public issue.

Report the problem privately to the repository owner through a private GitHub channel where available. Include:

- the affected file, component, or workflow;
- steps required to reproduce the issue;
- the expected and observed behaviour;
- the potential security impact;
- a minimal proof of concept that does not expose third-party data;
- any suggested mitigation.

Please remove API tokens, credentials, private keys, certificates, personal data, and production system details from reports and attachments.

## Scope

Security reports may concern:

- accidental inclusion of credentials or sensitive files;
- unsafe dependency or workflow configuration;
- command execution or path-handling weaknesses in repository scripts;
- misleading cryptographic guidance that could encourage unsafe production use;
- notebook content that leaks local or personal information;
- integrity or provenance problems affecting reproducibility.

Educational toy algorithms, expected limitations of quantum simulators, and the absence of production hardening are not vulnerabilities by themselves when they are clearly documented.

## Responsible handling

The maintainer will assess valid reports, limit disclosure while a fix is prepared, and credit reporters when appropriate. No service-level response time is guaranteed for this educational repository.
