# Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: [6,8]

# Input: A = [100, 150, 150, 153], target = 150
# Output: [1,2]

# Input: A = [1,2,3,4,5,6,10], target = 9
# Output: [-1, -1]

class Solution: 
    def getRange(self, arr, target):
        start,end = -1,-1
        leng = len(arr)
        for index in range(leng):
            if arr[index] == target:
                if start == -1:
                    start = index
                else :
                    end = index
        return [start,end]
  
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))