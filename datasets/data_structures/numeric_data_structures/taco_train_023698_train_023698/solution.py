from collections import *
input()
s = k = 0
d = defaultdict(int)
for (i, q) in enumerate(map(int, input().split())):
	k += i * q - s + d[q + 1] - d[q - 1]
	s += q
	d[q] += 1
print(k)
