# AI for Programming

A BIO722P teaching repository exploring Git source control and AI-assisted
programming. It contains small Python examples and records of experiments and
prompting in `copilot_practical/`, alongside planning notes for a treated-versus-
control RNA-seq differential-expression comparison.

## Examples

The practical scripts demonstrate DNA/RNA translation, reverse complementation,
and FASTA GC-content reporting. The GC-content script reads multiple FASTA
records, skips empty sequences with a warning, and supports `--min-gc` to filter
for records above a GC-percentage threshold. `summary.md` introduces how its
`read_fasta()` and `main()` functions work.

Run the GC-content script from `copilot_practical/` with:

```sh
python3 scripts/gc_content.py input/test_seq.fasta
python3 scripts/gc_content.py --min-gc 50 input/test_seq.fasta
```

RNA-seq materials are planning notes and sample metadata, not an implemented
analysis pipeline. Sequencing data and generated results are kept separate from
the tracked teaching materials.

## Repository history

The history includes AI-assisted implementation and correction of sequence
translation and reverse-complement examples, recorded experiments with a local
Ollama model, and a merge resolving competing GC-output precision changes in
favor of two decimal places. `WHATIDID.txt` records prompts and work completed.
The analysis-notes branch records plans for the RNA-seq comparison.

At the time of writing, five named branches are present across local and remote
refs: `main`, `docs/ai-practical-readme`, `gc-precision`, `origin/main`, and
`origin/feature/add-analysis-notes`. Local `main` contains the merge that
resolved the GC precision conflict, and the documentation branch extends it.
`origin/main` still points to the competing four-decimal change.

```text
... -- common -- origin/main (4 decimal places) --\
          \-- gc-precision (2 decimal places) ----- merge (main) -- README (docs/ai-practical-readme)
```

The repository is a collection of learning examples and experiment records,
not a unified application; the planned RNA-seq workflow has not been
implemented.

Generated using GitHub Copilot; model: Auto mode (selected dynamically). Information may be false.