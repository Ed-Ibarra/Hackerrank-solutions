def average(array):
    return sum(set(array))/len(set(array))

if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)