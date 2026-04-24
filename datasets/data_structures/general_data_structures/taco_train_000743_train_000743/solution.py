from collections import Counter
t = int(input())
for i in range(0, t):
	n = int(input())
	a = list(map(int, input().split()))
	print(n - max(Counter(a).values()))
