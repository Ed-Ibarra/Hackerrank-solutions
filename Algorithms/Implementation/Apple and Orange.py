def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(1 for apple in apples if s <= a + apple <= t))
    print(sum(1 for orange in oranges if s <= b + orange <= t))

if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    _, _ = map(int, input().split())

    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)