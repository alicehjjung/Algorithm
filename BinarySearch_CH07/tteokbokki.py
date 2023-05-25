#떡볶이 떡 만들기
"""
4 6
19 15 10 17
"""
#input
N,M = map(int,input().split())
array=list(map(int,input().split()))

def chop(num):
    new=[]
    for i in array:
        if i<num:
            new.append(0)
        else:
            new.append(i-num)
                
    if sum(new)==M:
        print(num)
        return num
    else:
        chop(num-1)

chop(max(array))