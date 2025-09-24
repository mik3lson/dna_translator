from flask import Flask, render_template,request,url_for

app= Flask(__name__)


#Codon dictionary
codon_dict= {"UUU":"phe","UUC":"phe","UUA":"leu","UUG":"leu","UCU":"ser","UCC":"ser","UCA":"ser","UCG":"ser",
    "CUU":"leu","CUC":"leu","CUA":"leu","CUG":"leu","AUU":"ile","AUC":"ile","AUA":"ile","AUG":"met",
    "GUU":"val","GUC":"val","GUA":"val","GUG":"val","CCU":"pro","CCC":"pro","CCA":"pro","CCG":"pro",
    "ACU":"thr","ACC":"thr","ACA":"thr","ACG":"thr","GCU":"ala","GCC":"ala","GCA":"ala","GCG":"ala",
    "UAU":"tyr","UAC":"tyr","CAU":"his","CAC":"his","CAA":"gln","CAG":"gln","AAU":"asn","AAC":"asn",
    "AAA":"lys","AAG":"lys","GAU":"asp","GAC":"asp","GAA":"glu","GAG":"glu","UGU":"cys","UGC":"cys",
    "UCG":"trp","CGC":"arg","CGC":"arg","CGA":"arg","CGG":"arg","AGU":"ser","AGC":"ser","AGA":"arg",
    "AGG":"arg","GGU":"gly","GGC":"gly","GGA":"gly","GGG":"gly"}

@app.route('/')
def index():
    return render_template('index.html')


#defining a valid dna sequence
def valid_dna_sequence(sequence):
    valid_letters = {'A','T','G','C'}
    return set(sequence).issubset(valid_letters)



@app.route('/process', methods=['POST'])
def process_dna():
    # Get DNA sequence from form input
    dna_sequence = request.form.get('dna_sequence', '').strip().upper().replace('/n','').replace(' ','')
    
    #validate the dna_sequence
    if valid_dna_sequence(dna_sequence):
        pass
    else:
        return render_template('index.html', result ="Opps. This is an Invalid DNA sequence. The valid neuclotide bases in DNA are 'A','T','G','C")
        


    # Replace T with U to simulate RNA transcription
    rna_sequence = dna_sequence.replace('T', 'U')
    
    #find the start codon
    start_codon = rna_sequence.find("AUG")

    # create a codon sequence that extracts a sequence starting from AUG
    codon_sequence = rna_sequence[start_codon:] 
    
    if start_codon == -1:
        return render_template('index.html', result ="Your Dna sequence contains no start codon. Hence it does not code for a particular protein. ")
    
        
    #define the stop codons 
    stop_codons = ["UGA","UAA","UAG"]

    #Group the codon_sequence into codons (triplets) and stop at the stop codons
    codons = []
    for i in range(0, len(codon_sequence),3):
        codon = codon_sequence[i:3+i]
        if codon in stop_codons:
            break
        codons.append(codon)
        
       
    
    # Map codons to their values in the codon dictionary
    translated_protein = [codon_dict[codon] for codon in codons if codon in codon_dict]
       
    # Join the translated protein list into a string
    result = ', '.join(translated_protein)
    
    return render_template('index.html', result=result)

    
if __name__ == '__main__':
    app.run(host ='0.0.0.0',debug = True)

