a = [102,5,99,3,8,6,7,2]

def bubbleSort(a,reverse = False):
    length = len(a)
    for j in range(length-1):
        for i in range(length-1-j):
            if reverse : 
                if(a[i] < a[i+1]):
                    swap(a,i)
            else:
                if(a[i] > a[i+1]):
                    swap(a,i)
    return a

def swap(arr,i):
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    
print(bubbleSort(a))
print(bubbleSort(a,reverse=True))
