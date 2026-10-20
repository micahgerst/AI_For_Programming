#!/usr/bin/env python3
"""AI Generated code that translates a DNA sequence into a protein sequence"""
def translate(seq, seq_type='RNA', codon_table=None):
    # Standard codon table
    standard_codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    # Default to the standard codon table if none is provided
    if codon_table is None:
        codon_table = standard_codon_table
    
    # Normalize the sequence to uppercase
    seq = seq.upper()

    # If the sequence is DNA, transform it to RNA
    if seq_type == "DNA":
        seq = seq.replace("T", "U")
    
    # Initialize a list to store the protein sequences for all reading frames
    protein_sequences = []
    
    # Translate each reading frame
    for frame in range(3):
        protein_seq = []
        for i in range(frame, len(seq), 3):
            codon = seq[i:i+3]
            if codon in codon_table:
                protein_seq.append(codon_table[codon])
            else:
                protein_seq.append('?')  # Use '?' to indicate an unknown codon
        protein_sequences.append(''.join(protein_seq))
    
    return protein_sequences

# this sequence should return MILKYWAY*
my_seq="ATGATCCTAAAATACTGGGCGTACTAG"
my_seq_2="ATGGCCATTGTAATGGGC"
print(translate(my_seq, seq_type='DNA'))