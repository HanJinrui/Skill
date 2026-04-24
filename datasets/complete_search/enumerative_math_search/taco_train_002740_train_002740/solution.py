for s in [*open(0)][1:]:
	(x, y) = map(int, s.split())
	print((x | y > 0) + (int((d := ((x * x + y * y) ** 0.5))) < d))
