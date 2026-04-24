R = lambda : map(int, input().split())
(t,) = R()
while t:
	t -= 1
	(n, k) = R()
	a = (b, c) = [[], []]
	for x in sorted(R()):
		a[x > 0] += (abs(x),)
	print(2 * sum(b[::k] + c[::-k]) - max([0] + b[:1] + c[-1:]))
