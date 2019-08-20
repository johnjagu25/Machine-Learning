# You are given a positive integer N which represents the number of steps in a staircase. 
# You can either climb 1 or 2 steps at a time. Write a function that returns
# the number of unique ways to climb the stairs.
# Can you find a solution in O(n) time?
# N = 1, 1 way to climb: [1]
# N = 2, 2 ways to climb: [1, 1], [2]
# N = 3, 3 ways to climb: [1, 2], [1, 1, 1], [2, 1]
# N = 4, 5 ways to climb: [1, 1, 2], [2, 2], [1, 2, 1], [1, 1, 1, 1], [2, 1, 1]
def staircase(n):
    a, b = 1, 2
    if n> 0:
        for val in range(n - 1):
            a, b = b, a + b
    else:
        a = 0
    return a

print(staircase(4))
# 5
print(staircase(5))
# 8
print(staircase(0))
# 0b