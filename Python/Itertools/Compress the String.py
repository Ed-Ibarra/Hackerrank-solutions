from itertools import groupby

# Option 1
for number, lst in groupby(input()):
    print(f"({len(list(lst))}, {number})", end=" ")


# Option 2
#
# [print(f"({len(list(lst))}, {number})", end=" ") for number, lst in groupby(input())]


# Option 3
#
# result = [(len(list(lst)), int(number)) for number, lst in groupby(input())]
# print(*result)


# Option 4
#
# group = []
# piv = ""
#
# for i in range(len(S)):
#     if i+1 == len(S):
#         piv += S[i]
#         group.append(piv)
#         break
#     elif S[i+1] == S[i]:
#         piv += S[i]
#     else:
#         piv += S[i]
#         group.append(piv)
#         piv = ""
#
# for g in group:
#     print(f"({len(g)}, {g[0]}) ", end="")




# Input
# 1222311

# Output expected
# (1, 1) (3, 2) (1, 3) (2, 1)