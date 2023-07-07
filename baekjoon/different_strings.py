#서로 다른 부분 문자열의 개수
#https://www.acmicpc.net/problem/11478
line=input()
length=len(line)
new = []
for i in range(1,length+1):
    for j in range(0,length):
        new.append(line[j:j+i])
        
print(len(set(new)))
