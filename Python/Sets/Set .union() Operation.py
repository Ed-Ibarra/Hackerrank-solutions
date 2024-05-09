_ = int(input())
setN= set(input().split())
_ = int(input())
setB = set(input().split())

print(len(setB.union(setN)))

# setB.union(setN)) = setB | setN