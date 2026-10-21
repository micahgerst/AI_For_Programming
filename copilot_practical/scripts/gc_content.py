#!/usr/bin/env python3
"""Print the GC content of each sequence in a FASTA file."""

import argparse
import sys


def read_fasta(path):
    """Yield each FASTA header and its concatenated sequence."""
    header = None
    sequence_parts = []

    with open(path, encoding="utf-8") as fasta:
        for line in fasta:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence_parts)
                header = line[1:]
                sequence_parts = []
            elif header is not None:
                sequence_parts.append(line)

    if header is not None:
        yield header, "".join(sequence_parts)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate GC content for each record in a FASTA file."
    )
    parser.add_argument("fasta_file", help="path to the FASTA file")
    parser.add_argument(
        "--min-gc",
        type=float,
        help="only print records with GC content above this percentage",
    )
    args = parser.parse_args()

    for header, sequence in read_fasta(args.fasta_file):
        if not sequence:
            print(f"Warning: skipping empty sequence for >{header}", file=sys.stderr)
            continue
        gc_percent = 100 * sum(base in "GCgc" for base in sequence) / len(sequence)
        if args.min_gc is not None and gc_percent <= args.min_gc:
            continue
        print(f">{header}: {gc_percent:.2f}%")


if __name__ == "__main__":
    main()
