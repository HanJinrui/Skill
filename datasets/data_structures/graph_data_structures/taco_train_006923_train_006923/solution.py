from collections import *
(d, c) = (defaultdict(int), [])
for i in range(int(input())):
	(x, y) = map(int, input().split())
	c += [x, y]
	d[x] += y
	d[y] += x
(a, b) = [q for (q, k) in Counter(c).items() if k == 1]
q = 0
while a != b:
	print(a)
	(q, a) = (a, d[a] - q)
print(a)
