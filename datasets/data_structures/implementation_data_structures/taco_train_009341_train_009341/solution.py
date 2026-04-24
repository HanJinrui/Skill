f = open(0)
R = lambda : map(int, next(f).split())
(n, q) = R()
d = {}
i = v = r = 0
for x in R():
	r += x
	i += 1
	d[i] = x
while q:
	q -= 1
	(t, *x) = R()
	if t & 1:
		(i, x) = x
		r += x - d.get(i, v)
		d[i] = x
	else:
		d = {}
		(v,) = x
		r = v * n
	print(r)
