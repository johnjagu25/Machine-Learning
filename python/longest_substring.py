# You are given a string s, and an integer k. 
# Return the length of the longest substring in s that contains at most k distinct characters.

# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. 
# The answer should be 5.

# Here's a starting point:

def longest_substring_with_k_distinct_characters(s, k):
    lastChar = ''
    maxLength = highest_sub = 0
    flag = True
    strLength = len(s)
    l_index = 0
    dont_change=True
    while flag:
        dont_change=True                
        if l_index == strLength:
            break
        val = s[l_index]
        if maxLength >= k and maxLength > highest_sub:
            highest_sub = maxLength
        if maxLength >= k and val == lastChar:
            maxLength += 1
        elif val != lastChar and maxLength < k:
            lastChar = val
            maxLength += 1
        elif maxLength == k:
                l_index -= 1
                maxLength = 1
                lastChar = s[l_index-1]
                dont_change=False
        else:
            maxLength = 0

        if dont_change:
            l_index += 1
            lastChar = val
    return highest_sub

print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)

