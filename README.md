# DNA to protein sequence Translator

This Flask-based web application processes DNA sequences and simulates RNA transcription and protein translation. 
It validates the DNA sequence, identifies the start codon, groups the RNA sequence into codons, and translates it into the corresponding protein sequence based on a codon dictionary. 


## Principle
This is base on the central dogma of molecular biology i.e the transfer of genetic information from DNA to RNA and finally to proteins. The sequence of DNA is represented by letters A,T,G,C for the neuclotides Adenine, Thymine, Guanine and Cytosine respective. RNA on the otherhand is represented by A,T,G,U indicating Adenine, Thymine, Guanine and **Uracil** respectively. 


![central dogma](https://github.com/mik3lson/DNA-Translator/blob/main/static/central%20dogma.png)

During Trancription DNA sequence is converted RNA sequence , subsequently the RNA sequences are converted to Protein (sequence of amino acids) through a process called Translation. Scientists and researchers have long investigated the DNA from an organism's genome to determine the likelihood of the organism to produce a specific protein of interest. Tools like this aid researchers and biologist in achieveing this goal.


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
- Biopython

## project structure
```

├── templates/
|   └── home.html
|   └── result.html
├── static/
|   └── img/
│   └── css/
|          └── index.css
|          └── result.css
├── requirements.txt
├── app.py
└── README.md

```


## Set up 

Clone the repository
```bash
git clone git@github.com:mik3lson/dna_translator.git
cd dna_translator
```

Create a virtual environment
```bash
python m venv .venv
.venv/Scripts/activate #for windows
.venv/bin/activate #for linux & windows 
```


Install dependencies
```bash
pip install requirements.txt
```

live: [dna-translator](https://dna-2-protein-translator.vercel.app/)
