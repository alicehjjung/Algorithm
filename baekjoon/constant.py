#상수
#https://www.acmicpc.net/problem/2908
A,B=input().split()

if int(A[2])>int(B[2]):
    print(A[2]+A[1]+A[0])
elif int(A[2])<int(B[2]):
    print(B[2]+B[1]+B[0])
else:
    if int(A[1])>int(B[1]):
        print(A[2]+A[1]+A[0])
    elif int(A[1])<int(B[1]):
        print(B[2]+B[1]+B[0])
    else:
        if int(A[0])>int(B[0]):
            print(A[2]+A[1]+A[0])
        elif int(A[0])<int(B[0]):
            print(B[2]+B[1]+B[0])
