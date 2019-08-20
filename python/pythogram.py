def findPythagoreanTriplets(nums):
    test =[]
    for val in range(0,len(nums)-1):
        for val2 in range(val+1,len(nums)):
            test.append(nums[val]**2 + nums[val2]**2)
    print(test)
    for val in nums:
        if val**2 in test:
            return val
    return False


print(findPythagoreanTriplets([12,3, 5, 11,4,7,25,10]))

3 - 12 + 5 , 5 + 13
12 - 5 + 13, 13 + 3
5 - 13 + 3 , 3 + 12
13 - 3 + 12 , 12 + 5
# True
