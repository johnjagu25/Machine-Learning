class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __repr__(self):
    return f"({self.value}, {self.next})"


def remove_dup(lst): 
        temp = lst
        if temp is None: 
            return
        while temp.next is not None: 
            if temp.value == temp.next.value: 
                new = temp.next.next
                temp.next = new 
            else: 
                temp = temp.next 


  # Fill this in.

lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))

remove_dup(lst)
print(lst)
# (1, (2, (3, None)))