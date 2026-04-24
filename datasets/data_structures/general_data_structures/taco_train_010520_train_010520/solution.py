R = lambda : map(int, input().split())
t = int(input())
for _ in range(t):
	(n, q) = R()
	a = [None, 0]
	i = 1
	for x in R():
		a.append(a[-1] + x * i)
		i = -i
	for _ in range(q):
		(p, q) = R()
		print((a[q] - a[p]) * (1 - q % 2 * 2) if (p ^ q) & 1 else 'UNKNOWN')
