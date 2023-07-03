#럭키 스트레이트
"""
input:
123402
output:
LUCKY
"""
#input
N=list(map(int,input()))
length=len(N)//2
sum1=sum(N[:length])
sum2=sum(N[length:])

if sum1==sum2:
    print("LUCKY")
else:
    print("READY")
