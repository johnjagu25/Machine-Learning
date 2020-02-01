# Given a list of words, group the words that are anagrams of each other. 
# (An anagram are words made up of the same letters).

# Example:

# Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
# Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

# Here's a starting point:

from collections import defaultdict

def groupAnagramWords(strs):
    anagram_hash = defaultdict(list)
    for val in strs:
        value = str(sorted(val))
        anagram_hash[value].append(val)
    return list(anagram_hash.values())

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]