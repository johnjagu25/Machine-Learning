k = 18
l = [4,5,1,2,6,3,8,10]

t_sum = 0
start = 0
i = 0
while t_sum < k and i < len(l):
    t_sum += l[i]
    while t_sum > k :
        t_sum -= l[start]
        start += 1
    i += 1

if t_sum == k:
    print(start,i-1)
else:
    print("No sum found")
    
    
    