_ = int(input())
setA = set(int(x) for x in input().split())

# Option 1
for _ in range(int(input())):
    instruction = list(input().split())
    setB = set(int(x) for x in input().split())

    if instruction[0] == "intersection_update":
        setA.intersection_update(setB)
    if instruction[0] == "update":
        setA.update(setB)
    if instruction[0] == "symmetric_difference_update":
        setA.symmetric_difference_update(setB)
    if instruction[0] == "difference_update":
        setA.difference_update(setB)

print(sum(setA))


# Option 2
#
# for _ in range(int(input())):
#     instruction, _ = list(input().split())
#     setB = set(int(x) for x in input().split())
#
#     eval(f"setA.{instruction}({setB})")
#
# print(sum(setA))