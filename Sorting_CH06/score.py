#성적이 낮은 순서로 학생 출력하기
"""
input:
2
홍길동 95
이순신 77
output:
이순신 홍길동
"""
#input
N=int(input())
students=[]
for i in range(N):
    name, score=input().split()
    students.append((name,int(score)))

#insertion sort
for i in range(N):
    for j in range(i,0,-1):
        if students[j][1]<students[j-1][1]:
            students[j],students[j-1]=students[j-1],students[j]

#sorted
#students=sorted(students, key=lambda student: student[1])

#print
for i in students:
    print(i[0],end=' ')