_ = int(input())
setN = set(input().split())
_ = int(input())
setB = set(input().split())

print(len(setB.intersection(setN)))

# setB.intersection(setN) = setB & setN