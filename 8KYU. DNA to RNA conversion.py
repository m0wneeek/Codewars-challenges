#DNA to RNA conversion
#Create a function which translates a given DNA string into RNA.

def dna_to_rna(dna):
    if "T" in dna:
        dna = dna.replace("T", "U")
    return dna
