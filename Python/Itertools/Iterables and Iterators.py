from itertools import combinations

# Length of the list
_ = int(input())

# Letters space-separated
letters = input().split()

# Number of indices
K = int(input())

# Indices combinations
com = [*combinations(letters, K)]

# The times that "a" appears in every combination
N = (sum(1 for pair in com if pair.count("a") >= 1))

# Print the probability of found an "a" in all possible combinations
print(N/len(com))



"""

Input
4 
a a c d
2

Output expected
0.8333333333333334

"""