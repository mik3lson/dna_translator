from flask import Flask, render_template,request,url_for, session
import os
from dotenv import load_dotenv


load_dotenv()


app= Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

#Codon dictionary
codon_dict= {"UUU":"phe","UUC":"phe","UUA":"leu","UUG":"leu","UCU":"ser","UCC":"ser","UCA":"ser","UCG":"ser",
    "CUU":"leu","CUC":"leu","CUA":"leu","CUG":"leu","AUU":"ile","AUC":"ile","AUA":"ile","AUG":"met",
    "GUU":"val","GUC":"val","GUA":"val","GUG":"val","CCU":"pro","CCC":"pro","CCA":"pro","CCG":"pro",
    "ACU":"thr","ACC":"thr","ACA":"thr","ACG":"thr","GCU":"ala","GCC":"ala","GCA":"ala","GCG":"ala",
    "UAU":"tyr","UAC":"tyr","CAU":"his","CAC":"his","CAA":"gln","CAG":"gln","AAU":"asn","AAC":"asn",
    "AAA":"lys","AAG":"lys","GAU":"asp","GAC":"asp","GAA":"glu","GAG":"glu","UGU":"cys","UGC":"cys",
    "UCG":"trp","CGC":"arg","CGC":"arg","CGA":"arg","CGG":"arg","AGU":"ser","AGC":"ser","AGA":"arg",
    "AGG":"arg","GGU":"gly","GGC":"gly","GGA":"gly","GGG":"gly"}

#protein string dictionary
prot_string ={"phe":"F","leu":"L","ser":"S","ile":"I","met":"M","val":"V","pro":"P","thr":"T","ala":"A","tyr":"Y",
              "his":"H","gln":"Q","asn":"N","lys":"K","asp":"D","glu":"E","cys":"C","trp":"W","arg":"R","gly":"G"}


def valid_dna_sequence(sequence):
    valid_letters = {'A','T','G','C'}
    return set(sequence).issubset(valid_letters)



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/process', methods=['POST'])
def process_dna():
    dna_sequence = request.form.get('dna_sequence', '').strip().upper().replace('\n','').replace('\r','').replace(' ','')

    if valid_dna_sequence(dna_sequence):
        pass
    else:
        return render_template('result.html', result ="Opps. This is an Invalid DNA sequence. The valid neuclotide bases in DNA are 'A','T','G','C")
    
    rna_sequence = dna_sequence.replace('T', 'U')
    
    start_codon = rna_sequence.find("AUG")

    # create a codon sequence that extracts a sequence starting from AUG
    codon_sequence = rna_sequence[start_codon:] 
    
    if start_codon == -1:
        return render_template('result.html', result ="Your Dna sequence contains no start codon. Hence it does not code for a particular protein. ")
    
    stop_codons = ["UGA","UAA","UAG"]

    #Group the codon_sequence into codons (triplets) and stop at the stop codons
    codons = []
    for i in range(0, len(codon_sequence),3):
        codon = codon_sequence[i:3+i]
        if codon in stop_codons:
            break
        codons.append(codon)

    # Map codons to their amino acid values in the codon dictionary
    translated_protein = [codon_dict[codon] for codon in codons if codon in codon_dict]
       
    result = ', '.join(translated_protein)
    session['result'] = translated_protein

    #finding the protSting equivalent of the protein sequence
    protString =""
    for prot in translated_protein:
        protString += prot_string[prot]
    
    return render_template('result.html', result=result, dna_sequence=dna_sequence, rna_sequence=rna_sequence, protString=protString)
    

if __name__ == '__main__':
    app.run(host ='0.0.0.0',debug = True)

