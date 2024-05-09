def is_leap(year):
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

    # Option 2
    #
    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         return year % 400 == 0
    #     return True
    # else:
    #     return False


    # Option 3
    #
    # if year % 4 != 0:
    #     return False
    #
    # if year % 4 == 0 and year % 100 != 0:
    #     return True
    #
    # if year % 100 == 0 and year % 400 == 0:
    #     return True
    #
    # if year % 100 == 0 and year % 400 != 0:
    #     return False

if __name__ == '__main__':

    print(is_leap(int(input())))