def count_unrooted_binary_trees(n):
    if n % 2 == 0:
        return 0
    
    def catalan_number(n):
        if n == 0:
            return 1
        c = [0] * (n + 1)
        c[0] = 1
        for i in range(1, n + 1):
            c[i] = 0
            for j in range(i):
                c[i] += c[j] * c[i - 1 - j]
        return c[n]

    return catalan_number((n - 1) // 2)


nodes = 7
print(count_unrooted_binary_trees(nodes))