# DNA-Translator


This Flask-based web application processes DNA sequences and simulates RNA transcription and protein translation. It validates the DNA sequence, identifies the start codon, groups the RNA sequence into codons, and translates it into the corresponding protein sequence based on a codon dictionary

## Features

- **DNA Sequence Validation:** Ensures that the input contains only valid nucleotide bases (`A`, `T`, `G`, `C`).
- **RNA Transcription:** Converts the DNA sequence into RNA by replacing `T` with `U`.
- **Protein Translation:**  
  - Identifies the start codon (`AUG`) to begin translation.
  - Groups the RNA sequence into triplets (codons).
  - Stops translation at the first stop codon (`UGA`, `UAA`, `UAG`).
  - Maps codons to amino acids using a codon dictionary.

- **Error Handling:**  
  - Detects invalid DNA sequences.
  - Alerts if the RNA sequence does not contain a start codon.

## Requirements

- Python 3.7 or higher  
- Flask 2.x  

