# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5, 
# return true since 4 + 1 = 5.

def two_sum(arr, k) :
    s = set()
    for val in range(0,len(arr)):
        temp = k - arr[val]
        if temp in s:
            return True
        else:
            s.add(arr[val])
    return False
 
 
print(two_sum([4,7,1,-3,2], 5))
print(two_sum([10,15,3,7], 17))
print(two_sum([1, 4, 45, 6, 10, 8] ,7))
print(two_sum([1, 4, 45, 6, 10, 8] ,20))

  