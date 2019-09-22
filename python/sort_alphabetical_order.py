# Given a list of words, and an arbitrary alphabetical order,
#  verify that the words are in order of the alphabetical order.

# Example:
# Input:
# words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

# Output: False
# Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

# Example 2:
# Input:
# words = ["zyx", "zyxw", "zyxwy"],
# order="zyxwvutsrqponmlkjihgfedcba"

# Output: True
# Explanation: The words are in increasing alphabetical order

# Here's a starting point:
def getOrder(order):
    order_dict = {}
    for index,letter in enumerate(order):
        order_dict[letter] = index
    return order_dict

def isSorted(words, order):
    alphabet_order = getOrder(order)
    last_index = -1
    for val in words:
        letter = val[0]
        # if letter is not available in the given order, then stop the sort and return false
        word_index = alphabet_order[letter] if letter in alphabet_order else -1
        if word_index >= last_index:
            last_index = word_index
        else:
            return False
    return True

  # Fill this in.

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"],
               "zyxwvutsrqponmlkjihgfedcba"))
# True
print(isSorted(["john", "willson", "zyxwy"],
               "abcdefghijklmnopqrstuvwxy"))
# True