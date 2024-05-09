_ = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()

    if command[0] == "pop":
        s.pop()
    if command[0] == "remove":
        s.remove(int(command[1]))
    if command[0] == "discard":
        s.discard(int(command[1]))

print(sum(s))