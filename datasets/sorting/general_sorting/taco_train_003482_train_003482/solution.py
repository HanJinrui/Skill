from collections import *
R = lambda : map(int, input().split())
(n, k) = R()
r = []
for (l, m) in Counter(R()).items():
	r += ((m // i, l) for i in range(1, m + 1))
print(*(x for (_, x) in sorted(r)[-k:]))
