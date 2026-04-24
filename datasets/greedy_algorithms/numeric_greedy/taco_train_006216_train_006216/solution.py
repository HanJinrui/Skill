for _ in [*open(0)][1:]:
	(a, b) = map(int, _.split())
	print(0 - -a * b // 2)
