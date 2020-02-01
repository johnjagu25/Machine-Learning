def missing_positive(arr):
    minV = maxV = arr[0] 
    gap = 9999
    for val in range(1,len(arr)):
        value = arr[val]
        if value >= 0 and value != minV and value != maxV:
            if minV >  value:
                v = minV - value
                if gap > v and v > 1:
                    gap = minV - 1
                minV = value
            elif maxV < value:
                v = value - maxV 
                if gap > v and v > 1:
                    gap = maxV + 1
                maxv = value
    return gap

print(missing_positive([3, 4,5,8,-1,6, 1,2]))
print(missing_positive([1,2,0]))

