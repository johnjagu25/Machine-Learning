# You 2 integers n and m representing an n by m grid, 
# determine the number of ways you can get from the top-left to the bottom-right of the matrix y 
# going only right or down.

# Example:
# n = 2, m = 2

# This should return 2, since the only possible routes are:
# Right, down
# Down, right.
def _getrowandcol(n,m,target):
    r = int(target / m) 
    c = target % m
    return r,c

def num_ways(n, m,start,target):
    start_r1,start_c1 = _getrowandcol(n,m,start)
    target_r1,target_c2 = _getrowandcol(n,m,target)
    target_r1 - start_r1 , target_c2 - start_c1
    return target_r1 - start_r1 + target_c2 - start_c1

print(num_ways(3,3,0,5))
print(num_ways(2,2,0,3))
print(num_ways(4,4,0,10))