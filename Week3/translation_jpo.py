# inputfile = "dna.txt"
# f = open(inputfile, "r")
# seq = f.read()
# seq = seq.replace("\n", "")
# seq = seq.replace("\r", "")

def read_seq(inputfile):
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq


# prt = read_seq("Week3/protein.txt")
# dna = read_seq("Week3/dna.txt")
# prt == translate(dna[20:938])[:-1]

def translate(seq):
    """Translate a string containing a nucleotide sequence into a string containing the corresponding sequence of amino acids. Nucleiotides are trnaslated
    in triplets using the table dictionary; each amino acid
    is encoded with a string of lenth 1."""

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }

    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i: i + 3]
            protein += table[codon]
    print(protein)
    return protein

translate("AAA")
#check if the sequence you want to translate length is divisible by 3

    # loop over the sequence

# Final task: compare your translation to the official one obtained from the ncbi