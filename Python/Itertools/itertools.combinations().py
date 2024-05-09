"""
Combinations focus on the selection of elements from a set regardless of order.
The order of the elements is NOT important.
Know how many different ways we can sort
                    AB
    A,B,C :2  ->    AC          AB = BA
                    BC
"""
from itertools import combinations

A = [x for x in input().split()]

for i in range(1, int(A[1])+1):
    for perm in sorted(combinations(sorted(A[0]), i)):
        print("".join(perm))


# Input example
# HACK 2

# Output with "".join()
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

# Output without "".join()
# ('A',)
# ('C',)
# ('H',)
# ('K',)
# ('A', 'C')
# ('A', 'H')
# ('A', 'K')
# ('C', 'H')
# ('C', 'K')
# ('H', 'K')