# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5
# Here is a starting point:

def findKthLargest(nums, k):
    if not nums or len(nums) < k:
        return None
    elif len(nums) == 1:
        return nums[0]
    else :
        return sorted(nums)[k]
    
  # Fill this in.

print(findKthLargest([3, 5, 2, 4, 6, 8], 5))
# 5
