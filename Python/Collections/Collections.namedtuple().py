from collections import namedtuple

# Number of students
N = int(input())

# Create the namedtuple
s = namedtuple('Student', input().split())

# Sum all the values from the MARKS field_name and prints it
print(sum([int(s(*input().split()).MARKS) for i in range(N)]) / N)


"""

Input
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6


Output expected
78.0

"""