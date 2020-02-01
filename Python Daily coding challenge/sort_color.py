# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library’s sort function for this problem.

# Can you do this in a single pass?

# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Here's a starting point:

class Solution:
  def sortColors(self, nums):
      low,mid,high = [0,0,len(nums)-1]
      while mid<= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid],nums[high]  = nums[high] , nums[mid]
            high -= 1
      return nums

          

    # Fill this in.

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]