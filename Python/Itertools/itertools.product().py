"""
It refers to the possible combinations
                    AC
    A,B ->          AD
    C,D ->          BC
                    BD
"""
from itertools import product

A = map(int, input().split())
B = map(int, input().split())

for e in sorted(set(product(A,B))):
    print(e, end=" ")


# Input example
# 1 2
# 3 4

# Output
# (1, 3) (1, 4) (2, 3) (2, 4)