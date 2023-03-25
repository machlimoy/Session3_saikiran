d={"AUG":"Methionine",
   "UUU":"Phenylalanine",
   "UUA":"Leucine",
   "UUG":"Leucine",
   "UCU":"Serine",
   "UCC":"serine",
   "UCA":"Serine",
   "UCG":"Serine",
   "UAU":"Tyrosine",
   "UAC":"Tyrosine",
   "UGU":"Cysteine",
   "UGC":"Cysteine",
   "UGG":"Tryptophan",
   "UAA":"STOP",
   "UAG":"STOP",
   "UGA":"STOP"
}

def translate(codons):
    for i in d:
        if i==codons:
            print("Valid codon")
            break
    else:
        print("Invalid codon")
translate(input())
