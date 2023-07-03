#문자열 재정렬
"""
input:
K1KA5CB7
AJKDLSI412K4JSJ9D
output:
ABCKK13
ADDIJJJKKLSS20
"""
N=input()
letters=[]
num,count=0,0

for i in range(len(N)):
    if N[i].isalpha():
        letters.append(N[i])
    else:
        num+=int(N[i])
        count+=1

letters=sorted(letters)
letters="".join(i for i in letters)

if count!=0:
  print(letters+str(num))
else:
  print(letters)
