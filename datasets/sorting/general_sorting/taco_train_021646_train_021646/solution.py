R = lambda : map(int, input().split())
(t,) = R()
while t:
	t -= 1
	(n, h) = R()
	a = (*R(),)
	i = len(a)
	s = 0
	for x in sorted((y - x for (x, y) in zip(a, a[1:]))):
		if s + x * i > h:
			break
		s += x
		i -= 1
	print(0 - (s - h) // i)
