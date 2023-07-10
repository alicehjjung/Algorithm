#배수와 약수
#https://www.acmicpc.net/problem/5086
while True:
	A,B=map(int,input().split())
	if A==0 and B==0:
		break
	if A<B:
		if B%A==0:
			print("factor")
			continue
	else:
		if A%B==0:
			print("multiple")
			continue
		else:
			print("neither")
