

def mains():
    good_number = 0;
    good_list = []
    n = 8
    inp = [8,2,10,3,6,1,30,6,2]
    if(n > 0):
        for val in range(1,n):
            isGoodNo = True  
            for val2 in range(1,n):
                if(inp[val]>=inp[val2] and (inp[val]%inp[val2])>0):
                    isGoodNo = False
                    break
            if isGoodNo:
                good_list.append(inp[val])
                good_number += 1
        print(good_number)
mains()