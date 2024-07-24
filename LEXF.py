from itertools import product

def enumerate_kmers(alphabet, k):
    return product(alphabet, repeat=k)


alphabet = "ACGT"
k = 2
for kmer in enumerate_kmers(alphabet, k):
    print(''.join(kmer))