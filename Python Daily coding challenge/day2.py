# Input: "((()))"
# Output: True

# Input: "[()]{}"
# Output: True

# Input: "({[)]"
# Output: False

class Solution:
    def isValid(self, s):
        open_brace = ["{","(","["]
        close_brace = ["}",")","]"]
        start = -1
        stack = []
        for val in s:
            if val in ["{","(","["]:
                start_index = open_brace.index(val)
                stack.append(val)
            else :
                stack.append(val)
                close_index = close_index.index(val)
                if start_index == close_index :
                    stack.pop()
                    start -= 1

        return len(stack) == 0
# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))
  
s = ""
# should return True
print(Solution().isValid(s))
  
s = "([{}])()"
# should return True
print(Solution().isValid(s))

s= "((()))"
print(Solution().isValid(s))
# Output: True

s= "[()]{}"
print(Solution().isValid(s))
# Output: True

s= "({[)]"
print(Solution().isValid(s))
# Output: False