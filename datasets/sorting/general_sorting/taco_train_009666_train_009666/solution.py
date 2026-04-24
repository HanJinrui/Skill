f = lambda : map(int, input().split())
(n, s) = f()
(u, v) = ([], [])
for i in range(n):
	(d, a, b) = f()
	if a > b:
		u.append([a, b, d])
	else:
		v.append([b, a, d])

def g(t):
	t.sort(key=lambda q: q[1] - q[0])
	m = sum((d for (a, b, d) in t))
	k = s * (m // s)
	n = m - k
	x = y = z = 0
	for (a, b, d) in t:
		if k >= d:
			k -= d
			z += d * a
		elif k:
			z += k * a
			x = (d - k) * a
			y = (d - k) * b
			k = 0
		else:
			x += d * a
			y += d * b
	return (x, y, z, n)
(a, b) = (g(u), g(v))
d = a[0] + b[0] if a[3] + b[3] > s else max(a[0] + b[1], a[1] + b[0])
print(a[2] + b[2] + d)
