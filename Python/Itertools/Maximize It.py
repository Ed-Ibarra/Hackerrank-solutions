import itertools

# Save the first input
K, M = map(int, input().split())

# Create a list for each input
lst = []

# Save inputs one-by-one without the first element/digit
for _ in range(K):
    nl = list(map(int, input().split()))
    del nl[0]
    lst.append(nl)

# Create a combination list
com = list(itertools.product(*lst))

# Prints the highest value of each result of each combination -> (a^2 + b^2 + c^2 + ... + n^2) % M
print(max(*[(sum(j**2 for j in i) % M for i in com)]))
