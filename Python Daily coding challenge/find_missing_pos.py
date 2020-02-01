
def getFirstPosVal(arr):
  missing = None
  minv = maxv = arr[0]
  for val in range(1,len(arr)):
    value = arr[val]
    if value >= 0:
      diff = 0
      if missing == value:
        missing = value + 1
      elif minv > value:
        diff = minv - value - 1
        if diff > 0:
          missing = minv - diff
        minv = value
      elif maxv < value:
        diff = value - maxv - 1
        if diff > 0:
          missing = maxv + 1
        maxv = value
      elif missing == value:
        maxv = value
        missing = None
      else :
          missing = maxv - value - 1

      if not missing:
        missing = maxv + 1
       
  return  missing 
  

print(getFirstPosVal([2,1,0]))
print(getFirstPosVal([3,4,-1,1]))
print(getFirstPosVal([8,4,6,5]))
