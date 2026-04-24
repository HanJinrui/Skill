from collections import *
I = input
for _ in [0] * int(I()):
	a = Counter((I() for _ in [0] * int(I())))
	b = (*a,)
	print(sum((a[u + v] * a[x + y] for (i, (u, v)) in enumerate(b) for (x, y) in b[:i] if (x == u) ^ (v == y))))
