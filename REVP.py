def reverse_complement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna, min_length=4, max_length=12):
    n = len(dna)
    results = []
    for length in range(min_length, max_length + 1):
        for i in range(n - length + 1):
            substring = dna[i:i + length]
            if substring == reverse_complement(substring):
                results.append((i + 1, length)) 
    return results

dna_sequence = "AAGCTTCTTGGGAA"
palindromes = find_reverse_palindromes(dna_sequence)
for position, length in palindromes:
    print(position, length)