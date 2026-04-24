R = lambda : map(int, input().split())
(t,) = R()
for _ in [0] * t:
	(n, m) = R()
	a = [*R()]
	p = {*R()}
	i = 0
	for j in range(1, n + 1):
		if not {j} & p:
			a[i:j] = sorted(a[i:j])
			i = j
	print('YNEOS'[a > sorted(a)::2])
