R = lambda : map(int, input().split())
(t,) = R()
while t:
	t -= 1
	(n, k) = R()
	a = (*R(), 18)
	s = 0
	for (x, y) in zip(a, a[1:]):
		s += 10 ** x * max(0, min((d := (10 ** (y - x) - 1)), k + 1))
		k -= d
	print(s)
