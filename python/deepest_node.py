# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

# Example:

#     a
#    / \
#   b   c
#  /
# d

# The deepest node in this tree is d at depth 3.

# Here's a starting point:

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    # string representation
    return self.val


def deepest(node):
    def deepLevel(node):
        maxVal = 0
        if not node:
            return maxVal
        left_level = deepLevel(node.left)
        right_level = deepLevel(node.right)

        return max(left_level,right_level) + 1

    def deepest_node(node,level,value = []):
        if not node:
            return 0
        if level == 1:
            value.append(node.val)
        else:
            deepest_node(node.left,level - 1,value)
            deepest_node(node.right,level - 1,value)
        return value
    level = deepLevel(node)
    deepest_value = deepest_node(node,level)[-1]
    return (deepest_value,level)

    
  # Fill this in.

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)


