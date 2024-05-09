def wrapper(function):
    def inner_func(lst):
        # Update the original list as a ordered list, with the 10 last numbers of every entry
        lst = sorted([int(number[-10:]) for number in lst])

        # We will pass a list with the ordered numbers in +91 XXXX XXXX format as parameter
        function([f"+91 {str(number)[:5]} {str(number)[5:]}" for number in lst])

    # This is for execute the inner function
    return inner_func




# Output format
# +91 XXXX XXXX


# Input
#  07895462130
# 919875641230
#   9195969878

# Output
# +91 78954 62130
# +91 91959 69878
# +91 98756 41230

@wrapper
# The wrapper function is executed first and follow function was passed as parameter
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)



#     harvest
#     jocks
#     daunting
#     juggle = malabares
#     twinge = punzadas
#     Picked up
#     annoying = molesto
#     get rid of = deshacerse de...
#     run out of = se acabo el/la
#     selfless
#     forehead = frente
#     straw = popote
#     acknowledge
#     accomplishment
#     grown man = adulto
#     grief
#     cheer you up = animarte
#     silly