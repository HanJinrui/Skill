from collections import *
input()
a = defaultdict(list)
i = 1
for c in input():
	a[c] += (i,)
	i += 1
for _ in [0] * int(input()):
	d = Counter(input())
	print(max((a[c][d[c] - 1] for c in d)))
