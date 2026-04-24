from collections import Counter
for _ in range(int(input())):
	(n, k, d) = map(int, input().split())
	a = [int(x) for x in input().split()]
	c = Counter(a[:d])
	l = len(c)
	for i in range(n - d):
		c[a[i + d]] += 1
		c[a[i]] -= 1
		if c[a[i]] == 0:
			del c[a[i]]
		l = min(len(c), l)
	print(l)
