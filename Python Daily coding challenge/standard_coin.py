m = 19
n = sorted([5,10],reverse=True)

l = []
last_sum = 0
for i in range(len(n)):
    while n[i] <= m:
        m -= n[i]
        l.append(n[i])
if(m > 0):
    print("balance {}".format(m))
print(l)
    
