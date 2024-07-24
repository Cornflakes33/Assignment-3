from math import factorial

def count_unrooted_binary_trees(n):
    if n < 3:
        return 0
   
    def double_factorial(k):
        if k <= 1:
            return 1
        return k * double_factorial(k - 2)
    
    return double_factorial(2 * n - 5) // factorial(n - 2)


nodes = 7
print(count_unrooted_binary_trees(nodes))