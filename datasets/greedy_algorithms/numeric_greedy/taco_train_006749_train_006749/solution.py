R = lambda : [*map(int, input().split())]
for _ in [0] * R()[0]:
	(n, k) = R()
	print(sum(R()[(n - 1) // 2 * k::n // 2 + 1]))
