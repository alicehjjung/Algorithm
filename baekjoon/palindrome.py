#팰린드롬인지 확인하기
#https://www.acmicpc.net/problem/10988
sen=input()
length = len(sen)

if length%2==0 and sen[:length//2]==sen[:length//2-1:-1]:
	print(1)
elif length%2==1 and sen[:length//2]==sen[:length//2:-1]:
	print(1)
else:
	print(0)
