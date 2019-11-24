# Given an array of numbers, find the length of the longest increasing subsequence in the array. 
# The subsequence does not necessarily have to be contiguous.

# For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 
#  longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.



def longest_increasing_subsequence(arr):

    l_seq = []
    temp = []
    maxLength = 0
    arrLength = len(arr)
    for v in range(0,arrLength):
        last_Val = arr[0]
        temp = []
        temp.append(last_Val)
        for v1 in range(v,arrLength):
            if arr[v1] > last_Val :
                temp.append(arr[v1])
                last_Val = arr[v1]
        if(len(temp) > maxLength):
            l_seq = temp
            maxLength = len(l_seq)
    return maxLength,l_seq



print(longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))