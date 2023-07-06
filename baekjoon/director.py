#영화감독 숌
#https://www.acmicpc.net/problem/1436
#input
N = int(input())
count=0
num=666

#brute force
while True:
    if "666" in str(num):
        count+=1 
    if count==N:
        break
    num+=1
print(num)
