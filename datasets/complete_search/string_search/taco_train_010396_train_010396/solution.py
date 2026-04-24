from itertools import *
k = int(input().split()[1])
d = {}
for (c, g) in groupby(input()):
	d[c] = d.get(c, 0) + len(list(g)) // k
print(max(d.values()))
