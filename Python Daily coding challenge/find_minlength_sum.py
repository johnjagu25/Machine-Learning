# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
import math
class Solution:
  def minSubArrayLen(self, nums, s):
    numLength = len(nums)
    minSubArr = math.inf   
    for val in range(numLength):      
        t = nums[val]
        temp =[t]
        if t >= s and len(temp) < minSubArr :
                return 1
        for val2 in range(val+1,numLength):            
            t += nums[val2]
            temp.append(nums[val2])
            if t >= s and len(temp) < minSubArr :
                minSubArr = len(temp)
                temp = []
                break;
            
    if math.isinf(minSubArr):
        minSubArr = 0

    return minSubArr         

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
print(Solution().minSubArrayLen([1, 4, 45, 6, 0, 19], 51))
print(Solution().minSubArrayLen([1, 10, 5, 2, 7], 9))
print(Solution().minSubArrayLen([1, 11, 100, 1, 0, 200, 3, 2, 1, 250], 280))
print(Solution().minSubArrayLen([1, 2, 4], 8))




