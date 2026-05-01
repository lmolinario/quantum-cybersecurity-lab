# Setup Guide

This guide explains how to run the experiments in this repository.

## 1. Clone the Repository

```bash
git clone https://github.com/lmolinario/quantum-cybersecurity-lab.git
cd quantum-cybersecurity-lab
```

## 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run Simulator Experiments

```bash
python experiments/simulators/run_basic_circuits.py
python experiments/simulators/run_bell_states.py
python experiments/simulators/run_grover_toy.py
```

## 5. Open Jupyter

```bash
jupyter notebook
```

## 6. Notes

The current experiments use local Qiskit Aer simulation.

IBM Quantum hardware execution will be added later in a dedicated experimental section.
