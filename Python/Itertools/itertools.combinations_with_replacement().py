"""
They are combinations allowing the individual elements to be repeated more than once
                    AA
                    AB
    A,B,C :2  ->    AC
                    BB
                    BC
                    CC
"""
from itertools import combinations_with_replacement

A = [x for x in input().split()]

for perm in sorted(combinations_with_replacement(sorted(A[0]), int(A[1]))):
    print("".join(perm))

# Input example
# HACK 2

# Output with "".join()
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

# Output without "".join()
# ('A', 'A')
# ('A', 'C')
# ('A', 'H')
# ('A', 'K')
# ('C', 'C')
# ('C', 'H')
# ('C', 'K')
# ('H', 'H')
# ('H', 'K')
# ('K', 'K')