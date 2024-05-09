_ = int(input())
setM = set(input().split())
_ = int(input())
setN = set(input().split())

# Option 1
[print(item) for item in sorted([int(x) for x in setM.symmetric_difference(setN)])]

# Option 2
# new_set = [int(x) for x in setM.symmetric_difference(setN)]
#
# for item in sorted(new_set):
#     print(item)