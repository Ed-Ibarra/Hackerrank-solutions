# if __name__ == '__main__':
#     lst = []
#
#     for _ in range(int(input())):
#         commands = list(input().split())
#
#         if commands[0] == 'insert':
#             lst.insert(int(commands[1]), int(commands[2]))
#
#         if commands[0] == 'print':
#             print(lst)
#
#         if commands[0] == 'remove':
#             lst.remove(int(commands[1]))
#
#         if commands[0] == 'append':
#             lst.append(int(commands[1]))
#
#         if commands[0] == 'sort':
#             lst.sort()
#
#         if commands[0] == 'pop':
#             lst.pop()
#
#         if commands[0] == 'reverse':
#             lst.reverse()

if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        op, *num = input().split()
        num = [int(i) for i in num]
        if op == 'print':
            print(arr)
        else:
            func = getattr(arr, op)
            func(*num)