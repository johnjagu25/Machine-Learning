from collections import Counter
a = "tesiting realy works better"
print(Counter(a))

count={}
for c in a:
   count[c]=count.setdefault(c, 0)+1
print(count)