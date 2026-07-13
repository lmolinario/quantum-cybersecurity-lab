# Contributing

Contributions that improve the educational value, reproducibility, or security relevance of this repository are welcome.

## Contribution areas

Useful contributions include:

- corrections to explanations, examples, or references;
- reproducible Qiskit and simulator experiments;
- notebook validation and automation improvements;
- post-quantum cryptography examples;
- quantum-safe readiness guidance;
- tests, documentation, and accessibility improvements.

## Workflow

1. Create a focused branch from `main`.
2. Make one logically related change per pull request.
3. Run the relevant local checks.
4. Open a pull request describing the motivation, implementation, and validation performed.

Example:

```bash
git checkout -b docs/improve-topic
git add .
git commit -m "docs: improve topic explanation"
git push origin docs/improve-topic
```

## Local validation

Install the project dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the available checks:

```bash
python scripts/validate_notebooks.py
python experiments/simulators/run_basic_circuits.py
python experiments/simulators/run_bell_states.py
python experiments/simulators/run_grover_toy.py
```

When changing `scripts/crypto_inventory.py`, test it against a directory containing only non-sensitive sample files. Do not submit private keys, credentials, production certificates, or confidential inventory output.

## Notebook contributions

For notebook changes:

- keep cells deterministic where practical;
- explain expected results and limitations;
- avoid embedding credentials or personal data;
- remove unnecessary execution artifacts and large outputs;
- ensure the notebook remains valid JSON.

## Security and cryptography notes

Educational examples must clearly distinguish toy demonstrations from production-ready cryptography. Avoid presenting experimental or simplified implementations as suitable for operational use.

Potential vulnerabilities should not be disclosed in a public issue. Follow the repository's security reporting instructions when available.

## Pull-request checklist

- [ ] The change has a clear educational or technical purpose.
- [ ] Documentation and commands have been checked.
- [ ] Relevant scripts or experiments have been executed.
- [ ] No secrets, credentials, personal data, or generated private keys are included.
- [ ] Toy or experimental cryptography is labelled appropriately.
