f = lambda : map(int, input().split())
(n, k) = f()
p = list(f())
r = range
u = [l * l + l >> 1 for l in r(n + 1)]
v = [(i, j) for i in r(n) for j in r(i + 1, n)]
t = [[p[i] > p[j] for j in r(n)] for i in r(n)]
a = [[0] * n for i in r(n)]
b = [[0] * n for i in r(n)]
c = [[0] * n for i in r(n)]
for l in r(min(k, 1000)):
	for j in r(1, n):
		(s, x) = (0, a[j])
		for i in r(j):
			s += t[i][j]
			x[i + 1] = x[i] + s
	for i in r(n):
		(s, y) = (0, b[i])
		for j in r(n - 1, i, -1):
			s += t[i][j]
			y[j - 1] = y[j] + s
	for d in r(1, n):
		(s, z) = (0, c[d])
		for i in r(n - d):
			s += t[i][i + d]
			z[i + 1] = z[i] + s
	for (i, j) in v:
		d = j - i
		(x, y, z) = (a[j], b[i], c[d])
		s = t[i][j] * (u[i] + u[d - 1] + u[n - j - 1])
		s += x[j] - x[i] - x[d - 1]
		s += y[i] - y[j] - y[n - d]
		s += (i + 1) * (n - j) - z[n - d] + z[n - j - 1] + z[i]
		t[i][j] = s / u[n]
print(sum((t[i][j] for (i, j) in v)))
