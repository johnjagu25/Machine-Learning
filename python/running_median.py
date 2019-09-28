# You are given a stream of numbers. Compute the median for each new element .

# Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

# Here's a starting point:

def running_median(stream):
    response = [stream[0]]
    for index in range(1,len(stream)):
        arr = sorted(stream[0:index+1])
        arrLen = len(arr)
        median_index = (arr[arrLen//2] + arr[arrLen//2 - 1])/2 if arrLen%2 == 0 else arr[round(arrLen//2)]
        response.append(median_index)
    return response
print(running_median([2, 1, 4, 7, 2, 0, 5]))
# 2 1.5 2 3.0 2 2.0 2
