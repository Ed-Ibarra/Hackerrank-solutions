"""
It refers to the arrangement of all or some elements of a set in a specific order.
The order of the elements is important.
Know how many different ways we can sort
                    ABC
                    ACB
    A,B,C ->        BAC
                    BCA
                    CAB
                    CBA
"""
from itertools import permutations

A = [x for x in input().split()]

for perm in sorted(permutations(A[0], int(A[1]))):
    print("".join(perm))

# Input example
# HACK 2

# Output with "".join()
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

# Output without "".join()
# ('A', 'C')
# ('A', 'H')
# ('A', 'K')
# ('C', 'A')
# ('C', 'H')
# ('C', 'K')
# ('H', 'A')
# ('H', 'C')
# ('H', 'K')
# ('K', 'A')
# ('K', 'C')
# ('K', 'H')