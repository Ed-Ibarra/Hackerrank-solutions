from collections import Counter

# Option 1

# How many words there will be
n = int(input())
# List of each word
lst = [input() for _ in range(n)]

# Print how many unique words there are
print(len(Counter(lst)))
# Print the frequencies of each unique word
print(*list(Counter(lst).values()))


# Option 2
# lst = [input() for _ in range(int(input()))]
#
# print(len(Counter(lst)))
# [print(lst.count(each), end=" ") for each in Counter(lst)]


# Option 3
# n = int(input())
# lst = [input() for _ in range(n)]
#
# print(len(Counter(lst)))
# for each in Counter(lst):
#     print(lst.count(each), end=" ")
