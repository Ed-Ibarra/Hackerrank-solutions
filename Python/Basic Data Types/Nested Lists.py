if __name__ == '__main__':
    lst = []
    setA = set()

    for i in range(int(input())):
        lst.append([input(), float(input())])
        setA.add(lst[i][1])

    lst.sort()

    for pos in range(len(lst)):
        if lst[pos][1] == sorted(setA)[1]:
            print(lst[pos][0])