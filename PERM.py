from itertools import permutations

def enumerate_gene_orders(n):
    return permutations(range(1, n + 1))


n = 3
for perm in enumerate_gene_orders(n):
    print(' '.join(map(str, perm)))