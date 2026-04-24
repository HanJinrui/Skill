t = int(input())
for i in range(t):
	(n, m, k) = map(int, input().split(' '))
	r = {}
	c = {}
	sum = m * n * (m * n + 1) // 2
	ra = rp = ca = cp = 0
	for j in range(k):
		(q, x, v) = map(int, input().split(' '))
		if q == 0:
			sum += (m * m * (x - 1) + m * (m + 1) // 2) * (v - 1)
			sum += (ra + rp * (x - 1)) * (v - 1)
			ca += m * (x - 1) * r.get(x, 1) * (v - 1)
			cp += r.get(x, 1) * (v - 1)
			r[x] = r.get(x, 1) * v
		else:
			sum += (m * n * (n - 1) // 2 + n * x) * (v - 1)
			sum += (ca + cp * x) * (v - 1)
			ra += x * c.get(x, 1) * (v - 1)
			rp += m * c.get(x, 1) * (v - 1)
			c[x] = c.get(x, 1) * v
	print(sum % 1000000007)
