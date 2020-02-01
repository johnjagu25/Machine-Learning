arr = [1, 2, 3, 4, 5, 6, 7]
d = 4
n =7

def rotation(arr,d,n):
    return arr[d:n] + arr[:d]
    
print(rotation(arr,d,n))
