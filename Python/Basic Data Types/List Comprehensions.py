x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Option 1
print(list([i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n))


# Option 2
#
# nl = []
# for k in range(z + 1):
#     for j in range(y + 1):
#         for i in range(x + 1):
#             if i + j + k != n:
#                 nl.append([i, j, k])
#
# print(nl)


# Option 3
#
# nl = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
#
# print(nl)