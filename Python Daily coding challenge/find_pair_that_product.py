# find two integers that multiply to given number
# eg [2,4,1,6,5,10] find the pair for 20 if there return the pair else return None
from collections import defaultdict
def find_pair(arr,val):
    visited_element = defaultdict(bool)
    for value in arr:
        visited_element[value] = True
        quotient = val / value
        if visited_element[quotient]:
            return (int(quotient),value)
    return None

print(find_pair([2,4,1,6,8,10],11))
print(find_pair([2,4,1,6,8,10],20))
print(find_pair([2,4,1,5,8,10],50))
print(find_pair([2,4,1,6,8,20],87))
print(find_pair([2,4,1,6,8,11],88))
print(find_pair([2,4,1,6,8,10],10))