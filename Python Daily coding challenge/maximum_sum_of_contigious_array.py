# You are given an array of integers. 
# Find the maximum sum of all possible contiguous subarrays of the array.

# Example:

# [34, -50, 42, 14, -5, 86]

# Given this input array, the output should be 137. The contiguous subarray with
# the largest sum is [42, 14, -5, 86].

# Your solution should run in linear time.

# Here's a starting point:

def max_subarray_sum(arr):
    maxSum = maxSumTemp = 0
    r_index=s_index=l_index = 0
    for (i,val) in enumerate(arr):
        if maxSumTemp == 0 :
            r_index = i 
        maxSumTemp += val
        # set to zero when the total becomes negative
        maxSumTemp = max(0,maxSumTemp)
        if maxSumTemp > maxSum :
            maxSum = max(maxSum,maxSumTemp)
            l_index = i
            if r_index :
                s_index = i
                r_index = 0
    print(arr[s_index:l_index+1])
    return maxSum

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
#137
print(max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]))
#7
print(max_subarray_sum([2,-8,3,-2,4,-10]))