# You are given an array of k sorted singly linked lists.
# Merge the linked lists into a single sorted linked list and return it.

# Here's your starting point:
import copy
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    a,b = lists
    loop_over  = False
    currentNode,trav_node = (a,b) if a.val<b.val else (b,a)
    merge_node = root_node = Node(currentNode.val)
    while currentNode :
        if loop_over:
            currentNode = None
        else:
            if not currentNode.next:
                merge_node.next = trav_node
                loop_over = True
            elif not trav_node.val:
                merge_node.next = currentNode.next
                loop_over = True
            else:
                currentNode,trav_node = (currentNode.next,trav_node) if  currentNode.next.val < trav_node.val  else (trav_node,currentNode.next)
                merge_node.next = Node(currentNode.val)
                merge_node = merge_node.next
    return root_node

  # Fill this in.

a = Node(1, Node(3, Node(5,Node(10, Node(16)))))
b = Node(2, Node(4, Node(6,Node(8,Node(9)))))
print(merge([a, b]))
# 123456