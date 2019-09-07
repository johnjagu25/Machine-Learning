# Implement a queue class using two stacks.
# A queue is a data structure that supports the FIFO protocol (First in = first out). 
# Your class should support the enqueue and dequeue methods like a standard queue.

# Here's a starting point:

class Queue:
  def __init__(self):
      self.queue_list = []
    # Fill this in.
    
  def enqueue(self, val):
      self.queue_list.append(val)
    # Fill this in.

  def dequeue(self):
      if len(self.queue_list) > 0 :
    #       this is very slow for large number ideally it is recommended to use list for queue.
    #       Use queue from collections library
          return self.queue_list.pop(0)
      else :
          return None    
    # Fill this in.

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())