# You are given an array of integers. Return the length of the 
# longest consecutive elements sequence in the array.

# For example, the input array [100, 4, 200, 1, 3, 2] has the 
# longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.

def longest_consecutive(nums):
    num_hash = {}
    longest = -1
    for val in nums:
        num_hash[val] = True
    for i in range(len(nums)):
        cons = nums[i]
        while cons in num_hash:
            cons += 1
        length = cons - nums[i]
        if longest < length :
            longest = length
            maxVal = cons
            minVal = nums[i]
    return list(range(minVal,maxVal+1))

print(longest_consecutive([7,100, 4, 99 , 45, 6,9,5,10,2,0,11]))