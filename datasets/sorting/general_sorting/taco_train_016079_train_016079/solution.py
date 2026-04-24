def main():
	input()
	a = list(map(int, input().split()))

	def f(a):
		maxend = maxnow = 0
		for x in a:
			maxend = max(0, maxend + x)
			maxnow = max(maxnow, maxend)
		return maxnow
	f1 = lambda x: f((i - x for i in a))
	f2 = lambda x: f((x - i for i in a))
	Max = max((abs(i) for i in a))
	(L, R) = (-Max, Max)
	eps = 10 ** (-8)
	for i in range(100):
		m = (L + R) / 2
		(v1, v2) = (f1(m), f2(m))
		if abs(v1 - v2) < eps:
			break
		if v1 > v2:
			L = m
		else:
			R = m
	print(v1)
main()
