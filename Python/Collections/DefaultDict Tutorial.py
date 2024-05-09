from collections import defaultdict

# Size of A and B, respectively
n, m = map(int, input().split())

# Defaultdict of list
a = defaultdict(list)

# Append words and indices in the defaultdict "a"
for i in range(1, n + 1):
    a[input()].append(i)  # ->  defaultdict(<class 'list'>, {'a': [1, 2, 4], 'b': [3, 5]})

# Seek every input in the defaultdict, print its indices if exist, or -1 if don't
for _ in range(m):
    print(*a.get(input()) or [-1])

# Option 2
#
# Size of A and B, respectively
# n, m = map(int, input().split())
#
# # Create A and B list of words
# A = [input() for _ in range(n)]
# B = [input() for _ in range(m)]
#
# # Search the B's words into A and print its indices if exist, or -1 if don't
# for word in B:
#     if word not in A:
#         print(-1)
#     else:
#         [print(i+1, end=" ") for i in range(n) if word == A[i]]
#         print("")

"""

Input
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b

Output expected
1 2 4
3 5

"""