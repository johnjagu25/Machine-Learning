# You are given a singly linked list and an integer k. Return the linked list, 
 
# removing the k-th last element from the list. 

# Try to do it in a single pass and using constant space.

# Here's a starting point:

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
    result = []
    if k == head.val:
        head = head.next
    previous_node = head
    current_node = previous_node.next
    while current_node:
        if k == current_node.val:
            previous_node.next = current_node.next
            current_node = previous_node.next.next if previous_node.next else None
        else:            
            previous_node = current_node
            current_node = current_node.next
    return head
  # Fill this in

head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(1))))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 1)
print(head)
# [1, 2, 4, 5]