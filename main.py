#Translating RNA into Protein - derived from Rosalind.info
#https://rosalind.info/problems/prot/
import fileinput

def codon_convert(codon):
    amino_acids = {
        "UUU" : "F", "CUU": "L", "AUU" : "I", "GUU" : "V",
        "UUC" : "F", "CUC": "L", "AUC": "I", "GUC" : "V",
        "UUA" : "L", "CUA" : "L", "AUA" : "I", "GUA": "V",
        "UUG" : "L",  "CUG": "L",  "AUG" : "M",  "GUG": "V", 
        "UCU" : "S",   "CCU" : "P" , "ACU": "T" , "GCU" : "A",
        "UCC" : "S",  "CCC" : "P", "ACC" : "T", "GCC" : "A",
        "UCA" : "S",   "CCA" : "P", "ACA" : "T", "GCA" : "A",
        "UCG" : "S",   "CCG" : "P",  "ACG" : "T", "GCG" : "A",
        "UAU" : "Y",   "CAU" : "H",  "AAU" : "N", "GAU" : "D",
        "UAC" : "Y",   "CAC" : "H",  "AAC" : "N",  "GAC" : "D",
        "UAA" : "Stop", "CAA" : "Q",  "AAA" : "K", "GAA" : "E",
        "UAG" : "Stop",  "CAG" : "Q", "AAG" : "K", "GAG" : "E",
        "UGU" : "C",   "CGU" : "R", "AGU" : "S", "GGU" : "G",
        "UGC" : "C",   "CGC" : "R",  "AGC" : "S", "GGC" : "G",
        "UGA" : "Stop", "CGA" : "R", "AGA" : "R",  "GGA" : "G",
        "UGG" : "W", "CGG" : "R", "AGG" : "R", "GGG" : "G"} 

    return amino_acids[codon]
    

user_opt = input("Choose a method of input: \n 1. Text box \n 2. Import file \n ")
protein = ""


if user_opt == '1':
    inp = input("Enter RNA string strand: ")

    for x in range(0, len(inp), 3):
        codon = inp[x:x+3]
        amino = codon_convert(codon)
        if (amino == "Stop"):
            break
        protein = protein + amino

elif user_opt == '2':
    filename = input("Enter file name: ")

    for line in fileinput.input(files=filename):
        for x in range(0, len(line), 3):
            codon = line[x:x+3]
            amino = codon_convert(codon)
            if (amino == "Stop"):
                break
            protein = protein + amino

else:
    print("Must enter a valid input")

print("Protein Strand: ")
print(protein)