# Implement a class for a stack that supports all the regular functions (push, pop) 
# and an additional function of max() which returns the maximum element in the stack
# (return None if the stack is empty). Each method should run in constant time.


class MaxStack:
  def __init__(self):
      self.stack = []
      self.maxVal = [-1]
    # Fill this in.

  def push(self, val):
      if val > self.maxVal[-1]:
          self.maxVal.append(val)
      self.stack.append(val)
    # Fill this in.

  def pop(self):
    if len(self.stack)>0:
      popedVal = self.stack.pop()
      if popedVal == self.maxVal[-1]:
        self.maxVal.pop()
    else:
        return "no element found in stack"
    # Fill this in.

  def max(self):
    if len(self.stack)>0:
        return self.maxVal[-1]
    else : 
        return "no element found in stack"
          
    # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2
