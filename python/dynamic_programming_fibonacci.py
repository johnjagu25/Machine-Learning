memo = {}
def fibonacci(n):
    global memo
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



print(fibonacci(7))
