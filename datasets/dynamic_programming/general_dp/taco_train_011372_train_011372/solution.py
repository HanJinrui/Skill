from itertools import islice
import sys
for s in islice(sys.stdin, 2, None, 2):
	a = [*map(int, s.split())]
	m = 0
	r = len(a) * 2 - 1
	for (x, y, z) in zip(a, a[1:], a[2:]):
		if x < y > z:
			m = 0
		else:
			m += 1
			r += m
	print(r)
