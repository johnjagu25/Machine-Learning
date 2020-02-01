# You are given an array of intervals - that is, an array of tuples (start, end). 
# The array may not be sorted, and could contain overlapping intervals. 
# Return another array where the overlapping intervals are merged.

# For example:
# [(1, 3), (5, 8), (4, 10), (20, 25)]

# This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

# Here's a starting point:

def merge(intervals):
    sorted_intervals = sorted(intervals)
    result = [sorted_intervals[0]]
    resultl_index = 0
    for i,val in range(1,len(sorted_intervals)):
        if sorted_intervals[i][0] < result[resultl_index][0] and sorted_intervals[i][1] > result[resultl_index][1]:
            result.append()
        
    
  # Fill this in.
  
print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]