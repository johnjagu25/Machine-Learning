# Given a string, find the longest palindromic contiguous substring. 
# If there are more than one with the maximum length, return any one.

# For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
#  The longest palindromic substring of "bananas" is "anana".

def palindrome(value):
    pal = []
    sLen = len(value)
    lastVal = -1
    maxLength = 1
    res = None
    for v in range(sLen):
        lastVal = -1
        for v1 in range(v+1,sLen):
            if value[v] == value[v1]:
                lastVal = v1
        if lastVal > -1:
            slicedPalindrome = value[v:lastVal+1]
            slicedPalLen = len(slicedPalindrome)
            if slicedPalLen > maxLength :
                validPal = isValidPal(slicedPalindrome)
                if validPal:
                    maxLength = slicedPalLen
                    res = slicedPalindrome
    return res

        
def isValidPal(palindrome):
    pLength = len(palindrome)
    for v in range(0,pLength):
        if palindrome[v] != palindrome[pLength-1 - v]:
            return False
    return True

print(palindrome("anana"))
print(palindrome("aabcdcb"))            
print(palindrome("aabkpdcb")) 
print(palindrome("nts"))