# Given an array of strictly the characters 'R', 'G', and 'B', 
# segregate the values of the array so that all the Rs come first, 
# the Gs come second, and the Bs come last. You can only swap elements of the array.

# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], 
# rbgrbrg
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def sort_rgb(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 'R':
            arr[low],arr[mid] = arr[mid],arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid],arr[high] = arr[high],arr[mid]
            high -= 1
    return arr
print(sort_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print(sort_rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G','B','R','R']))

def sor_rgb_without_swap(arr):
    low = []
    mid = []
    high = []
    for val in arr:
        if val == 'R':
            low.append(val)
        elif val == 'G':
            mid.append(val)
        else:            
            high.append(val)
    return low+mid+high

print(sor_rgb_without_swap(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
print(sor_rgb_without_swap(['G', 'B', 'R', 'R', 'B', 'R', 'G','B','R','R']))