def create_character_table(dna):
    table = {}
    for char in dna:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
    return table


dna_sequence = "AAGCTTCTTGGGAA"
char_table = create_character_table(dna_sequence)
for char in sorted(char_table):
    print(f"{char}: {char_table[char]}")