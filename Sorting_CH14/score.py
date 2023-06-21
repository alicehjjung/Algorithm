#국영수
"""
input:
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
output:
Donghyuk
Sangkeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
"""
#input
N=int(input())
students=[]
for i in range(N):
    tmp=list(input().split())
    tmp[1],tmp[2],tmp[3]=int(tmp[1]),int(tmp[2]),int(tmp[3])
    students.append(tuple(tmp))

#sorting
students.sort(key=lambda x: (-x[1],x[2],-x[3],x[0]))
for i in range(N):
    print(students[i][0])
