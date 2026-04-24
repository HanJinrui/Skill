from collections import defaultdict
from math import gcd
from functools import lru_cache
t = int(input())

@lru_cache(None)
def rf(x, y):
	g = gcd(x, y)
	y = y // g
	x = x // g
	x -= y * (x // y)
	return (x, y)

def solve(N):
	nums = [x for x in range(1, N + 1)]
	ans = 0
	d = defaultdict(int)
	for x in nums:
		for y in nums:
			(sx, sy) = rf(x, y)
			d[sx, sy] += 1
	for (k, v) in d.items():
		(sx, sy) = k
		if sx > 0:
			nsx = sy - sx
		else:
			nsx = sx
		ans += d[nsx, sy] * d[sx, sy]
	print(ans)
while t:
	N = int(input())
	solve(N)
	t -= 1
