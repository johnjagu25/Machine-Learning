def second_largest(arr):
    if len(arr) < 2:
        return False
    first = max(arr[0],arr[1])
    second = min(arr[0],arr[1])
    for val in range(2,len(arr)):
        if arr[val] > first :
            second = first
            first = arr[val] 
        elif arr[val] > second :
            second = arr[val]
    return second

arr = [1,4,78,23,99,43,2,98,101,102]
print(second_largest(arr))