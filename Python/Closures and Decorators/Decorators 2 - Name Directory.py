import operator

def person_lister(function):
    def inner_func(people):
        # This sorts the content of the "people" parameter by 3rd column
        # people.sort(key=operator.itemgetter(2))

        # You can also do the sort process in the for loop, with no import libraries
        # sorted(people, key=lambda x: int(x[2]))
        for person in sorted(people, key=lambda x: int(x[2])):
            yield function(person)

    # This is for execute the inner function
    return inner_func

@person_lister
# The wrapper function is executed first and next function is passed as parameter
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')