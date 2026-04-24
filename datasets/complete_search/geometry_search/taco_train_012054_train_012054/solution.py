from fractions import Fraction
from math import inf
n = int(input())
p = []
q = set()
for i in range(n):
	(x, y) = [int(i) for i in input().split()]
	for (j, k) in p:
		try:
			m = Fraction(k - y, j - x)
			c = Fraction(y - m * x)
		except ZeroDivisionError:
			(m, c) = (inf, x)
		q.add((m, c))
	p += [(x, y)]
q = list(q)
i = 0
k = len(q)
res = 0
while i < k:
	j = i + 1
	while j < k:
		if q[i][0] != q[j][0]:
			res += 1
		j += 1
	i += 1
print(res)
