R = lambda : [*map(int, input().split())]
for _ in [0] * R()[0]:
	(a, b, *_, c) = sorted((R() for _ in [0] * R()[0]))
	print(*(c[:1] + a, a[:1] + c)[a[0] == b[0]])
