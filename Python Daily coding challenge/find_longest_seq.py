# Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.
# Input: [1, 3, 5, 3, 1, 3, 1, 5]
# Output: 4

def findSequence(seq):
    length = len(seq)
    if length > 1:
        largest = 2
        count = 0
        for val in range(length-2):
            s = seq[val]
            e = seq[val+1]
            org = [s,e]
            switch = True
            for val2 in range(val+2,length):
                value = seq[val2]
                if switch :
                    if s != value:
                        org = []
                        break
                else:
                    if e != value:
                        org = []
                        break
                    org.append(s)
                    org.append(e)
                    temp = len(org)
                    if temp > largest:
                        largest = temp
                switch = not switch
        return largest


print(findSequence([ 3, 1, 3, 4,1, 3, 1, 5]))
# 4