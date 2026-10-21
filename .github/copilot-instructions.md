# Repository guidance

## Build, test, and lint

There is no configured build system, test runner, or linter. From the repository root:

- Run the DNA translator example: `python3 copilot_practical/scripts/translate_dna.py`
- Check one translation: `python3 -c "from copilot_practical.scripts.translate_dna import translate; assert translate('AUG')[0] == 'M'"`

The translator currently prints its hard-coded example at module load, including when imported by the focused check.

## Architecture

This is a small BIO722P teaching repository, not a single integrated application. `copilot_practical/` records experiments with a locally run Ollama model and contains a standalone DNA/RNA translation script. `rnaseq-pipeline-notes/` holds planning notes and sample metadata for a treated-versus-control differential-expression comparison; it does not currently contain a pipeline implementation. The root README describes the course/repository purpose.

## Code and data conventions

- `translate` uses RNA codons in its standard genetic code table. DNA input is uppercased and converted from T to U only when `seq_type="DNA"` is supplied; the function defaults to `"RNA"`.
- Translation returns one protein string for each of the three forward reading frames, and represents codons absent from the chosen table with `?`. A supplied `codon_table` replaces the standard table.
- Keep RNA-seq planning inputs and generated/large sequencing artifacts distinct: sample metadata is CSV, while `.bam`, `.fastq.gz`, `results/`, and `tmp/` are ignored by Git.
