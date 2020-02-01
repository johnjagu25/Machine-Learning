# Given a number of integers, combine them so it would create the largest number.

# Example:
# Input:  [17, 7, 2, 45, 72]
# Output:  77245217
from itertools import permutations 
from functools import reduce
def largest_num(arr): 
    maxVal = -1
    list_len = len(arr)
    for val in permutations(arr,list_len): 
        num = int("".join(map(str,val)))
        if num > maxVal :
            maxVal = num
    return maxVal
  
print(largest_num([500, 4, 199,32,365, 7])) 
# 7500436532199
print(largest_num([17, 7, 2, 45, 72]))
# 77245217
