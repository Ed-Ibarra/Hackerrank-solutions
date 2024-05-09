def count_substring(string, sub_string):
    # Option 1
    return sum(1 for i in range(len(string) - (len(sub_string)-1)) if string[i:i + len(sub_string)] == sub_string)

    # Option 2
    #
    # ss = []
    # for i in range(len(string) - (len(sub_string)-1)):
    #     if string[i:i + len(sub_string)] == sub_string:
    #         ss.append(string[i:i + len(sub_string)])
    # return len(ss)

    # Option 3
    #
    # cont, n = 0, 0
    #
    # while True:
    #     if string.find(sub_string, n) != -1:
    #         cont += 1
    #         n = string.find(sub_string, n) + 1
    #     else:
    #         return cont

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)