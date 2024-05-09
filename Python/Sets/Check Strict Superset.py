def isstrictsuperset(A, b):
    # True -> if every item on "b" exist on "a" AND if NOT every item on "a" exist on "b"
    return b.issubset(A) and not (A.issubset(b))


A = set(int(x) for x in input().split())
res = True

for _ in range(int(input())):
    b = set(int(x) for x in input().split())
    # It does the following logical operation: "res" AND "isstrictsuperset(a, b)"
    # In other words, storage the boolean result
    res &= isstrictsuperset(A, b)

print(res)