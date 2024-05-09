from collections import Counter

_ = int(input())
setA = list(int(x) for x in input().split())

# Prints the item repeats fewer times in a list
print(min(Counter(setA), key=Counter(setA).get))