# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given 3 sorted lists, find the intersection of those 3 lists.

# Here's an example and some starter code.

def intersection(list1, list2, list3):
    i=j=k = 0
    l1,l2,l3 = len(list1),len(list2),len(list3)
    comb = []
    while i < l1 and j < l2 and k < l3:
        if list1[i] == list2[j] and list2[j] == list3[k]:
            comb.append(list1[i])
            i += 1
            j += 1
            k += 1
        elif list1[i] < list2[j]:
            i += 1
        elif list2[j] < list3[k]:
            j += 1
        else :
            k += 1
    return comb



  # Fill this in.
  
print(intersection([1, 2, 3, 4,6], [2, 4, 6, 8], [ 4, 6]))
# [4]
