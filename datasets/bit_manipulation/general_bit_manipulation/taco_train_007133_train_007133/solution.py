from collections import *
R = lambda : [*map(int, input().split())]
for _ in [0] * R()[0]:
	a = []
	c = Counter()
	for _ in [0] * R()[0]:
		a += (R()[1:],)
		c.update(a[-1])
	print('YNeos'[all((any((c[x] < 2 for x in y)) for y in a))::2])
