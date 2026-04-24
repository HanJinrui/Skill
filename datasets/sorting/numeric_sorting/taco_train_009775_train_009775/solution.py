import math
a = lambda z: z < 1 or (i := math.isqrt(z)) * 2 + z // i - 1
for s in [*open(0)][1:]:
	(p, g) = map(int, s.split())
	print(a(g) - a(p - 1))
