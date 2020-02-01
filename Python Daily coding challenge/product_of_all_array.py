# Given an array of integers, return a new array 
# such that each element at index i of the new array is
#  the product of all the numbers in the original array except the one at i

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
#  the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?
from functools import reduce
def findProduct(arr):
    def divide(dividend, divisor):  
        sign = -1 if ((dividend < 0) ^  (divisor < 0)) else 1
        dividend = abs(dividend) 
        divisor = abs(divisor)     
        quotient = 0
        while (dividend >= divisor):  
            dividend -= divisor 
            quotient += 1          
        return sign * quotient 
    total_prod = reduce(lambda x,y:x*y , arr)
    return [divide(total_prod,val) for val in arr]

print(findProduct([1, 2, 3, 4, 5]))
print(findProduct([3, 2, 1]))