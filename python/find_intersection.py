# Given two arrays, write a function to compute their 
# intersection - the intersection means the numbers that are in both arrays.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:
# Each element in the result must be unique.
# The result can be in any order.

# Here's a starting point:
from functools import reduce
class Solution:
  def intersection(self, nums1, nums2):

      dict_obj = {}
      response = []
      for val in nums1:
          if val not in dict_obj:
              dict_obj[val] = 1
      for val in nums2:
          if val in dict_obj :
              dict_obj[val] += 1
              if dict_obj[val] == 2:
                  response.append(val)
      return response

    # Fill this in.

print(Solution().intersection([4, 9, 5, 8, 10], [9, 4, 9, 8, 4]))
# [9, 4]