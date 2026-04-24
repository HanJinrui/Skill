from collections import Counter
t = int(input())
for _ in range(t):
	input()
	d = Counter(map(int, input().split()))
	print(sum((d[j] >= i for i in d for j in range(1, d[i] + 1))))
