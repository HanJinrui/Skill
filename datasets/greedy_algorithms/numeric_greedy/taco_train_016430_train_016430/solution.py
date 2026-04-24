R = lambda : [*map(int, input().split())]
for _ in [0] * R()[0]:
	a = [R() for _ in [0] * R()[0]]
	r = 0
	for b in zip(a, a[::-1]):
		b = (*zip(*b),)
		for (x, y) in zip(b, b[::-1]):
			(u, v, x, y) = sorted(x + y)
			r += x + y - u - v
	print(r // 4)
