# Given an array nums, write a function to move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# Here is a starting point:

class Solution:
  def moveZeros(self, nums):

      lastIndex = 0
      for index,num in enumerate(nums):
          if num != 0 :
            nums[lastIndex] = num
            nums[index] = 0
            lastIndex += 1

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0,5]
nums1 = [0,1,0,3,12]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

Solution().moveZeros(nums1)
print(nums1)
# [1,3,12,0,0]