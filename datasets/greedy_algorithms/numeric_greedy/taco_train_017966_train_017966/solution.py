R = lambda : map(int, input().split())
(t,) = R()
while t:
	t -= 1
	(n,) = R()
	print(sum((abs(y - x) for a in zip(*map(sorted, zip(R(), R()))) for (x, y) in zip(a, a[1:]))))
