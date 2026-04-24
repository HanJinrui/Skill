from collections import Counter
for i in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	d = max(Counter(l).values())
	print(n - d)
