# You are given an array of integers and an integer value K .
# Return true if there exist two element A, B in the array So that A+B = K


L = [1,3,5,10,33,55]
k = 11

hashing = {}

def exists(k):
    arr_len = len(L)
    for i in range(arr_len):
        diff = k - L[i]
        if L[i] in hashing:
            return (diff,L[i])
        hashing.setdefault(diff,True)
    return "No pair available for the given number"
    

print(exists(k))
