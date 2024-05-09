from collections import Counter

# Number of shoes
_ = int(input())

# Shoe sizes in the shop (one size by couple shoe)
shoe_sizes = map(int, input().split())
count_sz = Counter(shoe_sizes)

# Number of customers
N = int(input())

# Shoe size desired by the customer and the prices of the shoe
cr = [list(map(int, input().split())) for _ in range(N)]

# How money owner earned
sales = 0

# Search the shoe size for each customer and if exist, sale it and delete the size of the Counter object
for i in range(N):
    if count_sz[cr[i][0]]:
        sales += cr[i][1]
        count_sz[cr[i][0]] -= 1

print(sales)


"""

Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Output expected
200

"""