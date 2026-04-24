t = int(input())
for i in range(t):
	n = int(input())
	l = list(map(int, input().split()))
	f = [0] * n
	for j in range(n):
		for k in range(j + 1, n):
			if l[j] > l[k]:
				f[j] += 1
				f[k] += 1
	w = sum(f) // 2
	p = [False] * (w + 1)
	p[0] = True
	for v in f:
		for z in range(w - v, -1, -1):
			p[z + v] |= p[z]
	print('YES' if p[w] else 'NO')
