
map={
    "AUG":"Methionine",
    "UUU":"Phenylalanine",
    "UUC":"Phenylalanine",
    "UUA":"Leucine",
    "UUG":"Leucine",
    "UCU":"Serine",
    "UCC":"Serine",
    "UCA":"Serine",
    "UCG":"Serine",
    "UAU":"Tyrosine",
    "UAC":"Tyrosine",
    "UGU":"Cysteine",
    "UGC":"Cysteine",
    "UGG":"Tryptophan",
    "UAA":"STOP",
    "UAG":"STOP",
    "UGA":"STOP",
}

def translate(condon):
    if(condon in map.keys()):
        return map[condon]
    raise Exception("Invalid codon")

print(translate("AUG"))