#!/usr/bin/env python3
"""Lightweight cryptographic inventory helper for quantum-safe readiness.

The script uses only the Python standard library. It does not certify that a
system is quantum-safe. It creates a first-pass inventory of files, key-material
indicators, and TLS endpoints that should be reviewed during PQC migration
planning.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import socket
import ssl
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

CRYPTO_EXTENSIONS = {
    ".pem",
    ".crt",
    ".cer",
    ".csr",
    ".key",
    ".pub",
    ".p12",
    ".pfx",
    ".jks",
    ".keystore",
    ".asc",
    ".gpg",
    ".kdbx",
}

TEXT_MARKERS = {
    "rsa_private_key": "BEGIN RSA PRIVATE KEY",
    "ec_private_key": "BEGIN EC PRIVATE KEY",
    "dsa_private_key": "BEGIN DSA PRIVATE KEY",
    "generic_private_key": "BEGIN PRIVATE KEY",
    "openssh_private_key": "BEGIN OPENSSH PRIVATE KEY",
    "certificate": "BEGIN CERTIFICATE",
    "certificate_request": "BEGIN CERTIFICATE REQUEST",
    "public_key": "BEGIN PUBLIC KEY",
    "ssh_rsa_public_key": "ssh-rsa",
    "ssh_ecdsa_public_key": "ecdsa-sha2-",
    "ssh_ed25519_public_key": "ssh-ed25519",
    "tls_rsa_cipher_hint": "TLS_RSA",
    "tls_ecdhe_cipher_hint": "TLS_ECDHE",
    "md5_hint": "MD5",
    "sha1_hint": "SHA1",
}

IGNORED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    "node_modules",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
}

MAX_TEXT_BYTES = 1024 * 1024


@dataclass(frozen=True)
class FileFinding:
    kind: str
    path: str
    indicator: str
    review_priority: str
    quantum_safe_note: str


@dataclass(frozen=True)
class TLSFinding:
    kind: str
    endpoint: str
    tls_version: str
    cipher_suite: str
    certificate_subject: str
    certificate_issuer: str
    review_priority: str
    quantum_safe_note: str


def iter_files(paths: list[Path]) -> Iterable[Path]:
    for root in paths:
        if root.is_file():
            yield root
            continue

        for current_root, dirnames, filenames in os.walk(root):
            dirnames[:] = [name for name in dirnames if name not in IGNORED_DIRS]
            for filename in filenames:
                yield Path(current_root) / filename


def read_text_prefix(path: Path) -> str:
    try:
        data = path.read_bytes()[:MAX_TEXT_BYTES]
    except OSError:
        return ""

    if b"\x00" in data[:4096]:
        return ""

    return data.decode("utf-8", errors="ignore")


def priority_for_marker(marker_name: str) -> str:
    if "private_key" in marker_name:
        return "high"
    if marker_name in {"ssh_rsa_public_key", "ssh_ecdsa_public_key"}:
        return "high"
    if marker_name in {"md5_hint", "sha1_hint"}:
        return "high"
    if marker_name == "certificate":
        return "medium"
    return "low"


def note_for_marker(marker_name: str) -> str:
    if "private_key" in marker_name:
        return "Private key material. Verify exposure, owner, rotation, and associated algorithm."
    if marker_name in {"ssh_rsa_public_key", "tls_rsa_cipher_hint"}:
        return "RSA should be included in the post-quantum migration inventory."
    if marker_name in {"ssh_ecdsa_public_key", "tls_ecdhe_cipher_hint"}:
        return "Elliptic-curve use should be included in the post-quantum migration inventory."
    if marker_name in {"md5_hint", "sha1_hint"}:
        return "Legacy hash indicator. Review independently from PQC migration."
    if marker_name == "ssh_ed25519_public_key":
        return "Modern classical signature key. Not considered post-quantum."
    if marker_name == "certificate":
        return "Certificate detected. Review key type, signature algorithm, CA, and renewal path."
    return "Potential cryptographic artifact. Review manually."


def classify_file(path: Path) -> list[FileFinding]:
    if path.name == Path(__file__).name:
        return []

    findings: list[FileFinding] = []

    if path.suffix.lower() in CRYPTO_EXTENSIONS:
        findings.append(
            FileFinding(
                kind="file_extension",
                path=str(path),
                indicator=path.suffix.lower(),
                review_priority="medium",
                quantum_safe_note="Cryptographic file or key-store extension. Review algorithm and migration constraints.",
            )
        )

    text = read_text_prefix(path)
    if not text:
        return findings

    upper_text = text.upper()
    for marker_name, marker in TEXT_MARKERS.items():
        haystack = upper_text if marker.isupper() else text
        if marker in haystack:
            findings.append(
                FileFinding(
                    kind="content_marker",
                    path=str(path),
                    indicator=marker_name,
                    review_priority=priority_for_marker(marker_name),
                    quantum_safe_note=note_for_marker(marker_name),
                )
            )

    return findings


def parse_endpoint(endpoint: str) -> tuple[str, int]:
    if ":" not in endpoint:
        return endpoint, 443
    host, port = endpoint.rsplit(":", 1)
    return host.strip(), int(port)


def format_name_tuple(value: object) -> str:
    if not value:
        return ""
    try:
        return ", ".join(f"{key}={field_value}" for item in value for key, field_value in item)  # type: ignore[union-attr]
    except Exception:
        return str(value)


def inspect_tls_endpoint(endpoint: str, timeout: float) -> TLSFinding:
    host, port = parse_endpoint(endpoint)
    context = ssl.create_default_context()

    with socket.create_connection((host, port), timeout=timeout) as raw_socket:
        with context.wrap_socket(raw_socket, server_hostname=host) as tls_socket:
            cipher = tls_socket.cipher()
            certificate = tls_socket.getpeercert()
            tls_version = tls_socket.version() or "unknown"
            cipher_suite = cipher[0] if cipher else "unknown"
            subject = format_name_tuple(certificate.get("subject")) if certificate else ""
            issuer = format_name_tuple(certificate.get("issuer")) if certificate else ""

    priority = "medium"
    note = "Review certificate key type, chain signatures, TLS version, and PQC or hybrid support."
    if tls_version in {"SSLv2", "SSLv3", "TLSv1", "TLSv1.1"}:
        priority = "high"
        note = "Legacy TLS version detected. Remediate before or alongside PQC planning."

    return TLSFinding(
        kind="tls_endpoint",
        endpoint=f"{host}:{port}",
        tls_version=tls_version,
        cipher_suite=cipher_suite,
        certificate_subject=subject,
        certificate_issuer=issuer,
        review_priority=priority,
        quantum_safe_note=note,
    )


def collect_findings(args: argparse.Namespace) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []

    for path in iter_files([Path(value) for value in args.path]):
        findings.extend(asdict(finding) for finding in classify_file(path))

    for endpoint in args.tls_endpoint:
        try:
            findings.append(asdict(inspect_tls_endpoint(endpoint, args.timeout)))
        except Exception as exc:
            findings.append(
                {
                    "kind": "tls_endpoint_error",
                    "endpoint": endpoint,
                    "tls_version": "",
                    "cipher_suite": "",
                    "certificate_subject": "",
                    "certificate_issuer": "",
                    "review_priority": "medium",
                    "quantum_safe_note": f"Could not inspect endpoint: {exc}",
                }
            )

    return findings


def write_json(findings: list[dict[str, str]], output: str | None) -> None:
    payload = json.dumps(findings, indent=2, sort_keys=True)
    if output:
        Path(output).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


def write_csv(findings: list[dict[str, str]], output: str | None) -> None:
    fieldnames = sorted({key for finding in findings for key in finding}) or [
        "kind",
        "path",
        "indicator",
        "review_priority",
        "quantum_safe_note",
    ]

    if output:
        output_file = Path(output).open("w", newline="", encoding="utf-8")
        close_output = True
    else:
        import sys

        output_file = sys.stdout
        close_output = False

    try:
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(findings)
    finally:
        if close_output:
            output_file.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a lightweight cryptographic inventory for PQC readiness.")
    parser.add_argument("--path", action="append", default=[], help="File or directory to scan. Defaults to '.'.")
    parser.add_argument("--tls-endpoint", action="append", default=[], help="TLS endpoint, for example example.com:443.")
    parser.add_argument("--timeout", type=float, default=5.0, help="Network timeout for TLS inspection.")
    parser.add_argument("--format", choices=("json", "csv"), default="json", help="Output format.")
    parser.add_argument("--output", help="Optional output file path.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if not args.path:
        args.path = ["."]

    findings = collect_findings(args)
    if args.format == "json":
        write_json(findings, args.output)
    else:
        write_csv(findings, args.output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
