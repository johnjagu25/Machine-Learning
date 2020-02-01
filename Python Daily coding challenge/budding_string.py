# Given two strings A and B of lowercase letters, 
# return true if and only if we can swap two letters in A so that the result equals B.

# Example 1:
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
# Input: A = "aa", B = "aa"
# Output: false
# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
# Input: A = "", B = "aa"
# Output: false
# Here's a starting point:

class Solution:
  def buddyStrings(self, a, b):

      len_a = len(a)
      len_b = len(b)
      if len_a != len_b:
          return False
      not_matching = []
      for val in range(0,len_a):
          if a[val] != b[val]:
              not_matching.append(val)              
          if len(not_matching) > 2:
              return False
      if len(not_matching) != 2:
          return False
      a = list(a)
      b = list(b)
      for val in not_matching:
          temp = a[val]
          a[val] = b[val]
          b[val] = a[val]
    
      return a == b
    # Fill this in.

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
print(Solution().buddyStrings('', 'aa'))
#False
print(Solution().buddyStrings('aa', 'aa'))
#False