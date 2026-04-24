from collections import Counter as C
import statistics as S
for _ in range(int(input())):
	n = int(input())
	print(min(S.multimode(C(list(map(int, input().split(' ')))).values())))
