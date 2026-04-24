from sys import stdin, stdout
g = stdin.readline

def f(j):
	p = k[j][:]
	while j:
		j -= j & -j
		for i in range(26):
			p[i] += k[j][i]
	return p
a = ord('a')
s = [ord(q) - a for q in g()[:-1]]
m = int(g())
n = len(s) + 1
k = [[0] * 26 for i in range(n)]
for (j, v) in enumerate(s, 1):
	while j < n:
		k[j][v] += 1
		j += j & -j
for i in range(m):
	(t, x, y) = g().split()
	if t == '1':
		(j, u) = (int(x), ord(y) - a)
		(v, s[j - 1]) = (s[j - 1], u)
		while j < n:
			k[j][u] += 1
			k[j][v] -= 1
			j += j & -j
	else:
		l = f(int(x) - 1)
		r = f(int(y))
		d = sum((v > u for (u, v) in zip(l, r)))
		stdout.write(str(d) + '\n')
