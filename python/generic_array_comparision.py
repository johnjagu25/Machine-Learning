A = ["India",100,30.10,"singapore"]
B = ["India",'Malaysia',1000,30.10]

def find_similar(a,b):
    hashing = {}
    for val in a:
        hashing[val] = True
    for val in b:
        if val in hashing:
            print(val)

find_similar(A,B)
