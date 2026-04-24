import sys
input = sys.stdin.readline
from collections import defaultdict
for _ in range(int(input())):
	(n, l, r) = map(int, input().split())
	(x, a, b) = [[*map(int, input().split())] for i in range(3)]
	d = defaultdict(int)
	gap = r - l
	for i in range(n):
		(d1, d2) = divmod(a[i], b[i])
		if d2:
			d[x[i] - d1 - 1 - gap] += d2
			d[x[i] + d1 + 1] += d2
		d[x[i] - d1 - gap] += b[i] - d2
		d[x[i] - gap] -= b[i]
		d[x[i]] -= b[i]
		d[x[i] + d1] -= d2 - b[i]
	(ans, now, rate, t) = (0, 0, 0, sorted(d.keys()))
	for i in range(len(t) - 1):
		(d0, d1, d2) = (t[i + 1], t[i], d[t[i]])
		rate += d2
		m = now + rate if d1 - r & 1 else 0
		now += (d0 - d1) * rate
		m = max(m, now - rate) if d0 - r & 1 else max(m, now)
		ans = max(ans, m)
	print(ans)
