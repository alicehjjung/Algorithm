#단어 공부
#https://www.acmicpc.net/problem/1157
from collections import Counter

word = input()
word = word.lower()

if len(word)==1:
    print(word.upper())
else:
    new = Counter(word).most_common(2)
    if new[0][1]==new[1][1]:
        print("?")
    else:
        print(new[0][0].upper())
