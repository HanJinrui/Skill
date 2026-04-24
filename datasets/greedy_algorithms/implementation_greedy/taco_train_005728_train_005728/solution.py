R = lambda : map(int, input().split())
(t,) = R()
for _ in [0] * t:
	(n, d) = R()
	r = i = 0
	for x in R():
		m = min(d, i * x)
		r += m // i if i else x
		d -= m
		i += 1
	print(r)
