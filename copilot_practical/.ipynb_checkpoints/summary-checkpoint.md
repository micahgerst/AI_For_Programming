## `scripts/gc_content.py`

The `read_fasta()` function reads a FASTA file one line at a time. When it
reaches a header line (starting with `>`), it groups the following sequence
lines together and yields the header with its complete sequence. This lets the
script handle records whose sequences span multiple lines.

The `main()` function handles command-line arguments, including the FASTA file
path and optional `--min-gc` threshold. It goes through each record from
`read_fasta()`, warns and skips records with empty sequences, then calculates
the percentage of bases that are G or C. It prints the record's header and
percentage unless the result is at or below the chosen threshold.
