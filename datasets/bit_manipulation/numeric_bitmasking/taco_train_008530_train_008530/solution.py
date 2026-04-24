import sys
from itertools import islice
from functools import reduce
from operator import xor
for s in islice(sys.stdin, 2, None, 2):
	(*b,) = map(int, s.split())
	x = reduce(xor, b) or min(b)
	if x:
		for i in range(len(b)):
			b[i] ^= x
	b.remove(0)
	print(*b)
