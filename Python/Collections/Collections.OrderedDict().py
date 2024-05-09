from collections import OrderedDict

# Number of items
N = int(input())

# Save all inputs in a list
lst = [input().split() for _ in range(N)]

# Take only the Net Price
np = [int(lst[i][-1]) for i in range(N)]

# Delete the last item from each list (Net Price) and join the rest
for i in range(N):
    lst[i].pop()
    lst[i] = " ".join(lst[i])

# Create the OrderedDict
od = OrderedDict()

# Save the item_name = Net Price * (times in lst)
for i in range(N):
    od[lst[i]] = np[i]*lst.count((lst[i]))

# Print the result
print(*(f"{k} {v}" for k, v in od.items()), sep="\n")



"""

Input
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30


Output expected
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

"""