#부품 찾기
"""
5
8 3 7 9 2
3
5 7 9
"""
#input
N=int(input())
N_list = list(map(int,input().split()))
M=int(input())
M_list = list(map(int,input().split()))

#if the item is in the list, print 'yes'
for i in range(M):
    if M_list[i] in N_list:
        print("yes",end=" ")
    else:
        print("no",end=" ")
