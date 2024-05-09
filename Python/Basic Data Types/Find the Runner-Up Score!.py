if __name__ == '__main__':
    n = int(input())

    # Option 1
    arr = set(map(int, input().split()))
    print(sorted(arr)[-2])

    # Option 2
    # print(sorted(set(map(int, input().split())))[-2])