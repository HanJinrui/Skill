from itertools import *
for s in [*open(0)][2::2]:
	a = [k for (k, g) in groupby(map(int, s.split()))]
	print('YNEOS'[sum((x > y < z for (x, y, z) in zip([2000000000.0] + a, a, a[1:] + [2000000000.0]))) > 1::2])
