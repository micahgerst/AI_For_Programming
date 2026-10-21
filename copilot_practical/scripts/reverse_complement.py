#!/usr/bin/env python3
# reverse_complement.py
# Reads a single-line DNA sequence from a FASTA file and prints its
# reverse complement.

COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C",
              "a": "t", "t": "a", "c": "g", "g": "c"}


def read_fasta_sequence(path):
    """Return the DNA sequence from a FASTA file, ignoring the header."""
    with open(path) as f:
        sequence_parts = []
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith(">"):
                continue
            sequence_parts.append(stripped)
    return "".join(sequence_parts)


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    normalized = seq.strip().upper()
    try:
        return "".join(COMPLEMENT[base] for base in reversed(normalized))
    except KeyError as error:
        raise ValueError(
            f"Invalid DNA sequence character: {error.args[0]!r}. "
            "Allowed characters are A, T, C, and G."
        ) from error

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: {sys.argv[0]} <fasta_file>")

    seq = read_fasta_sequence(sys.argv[1])
    print(reverse_complement(seq))