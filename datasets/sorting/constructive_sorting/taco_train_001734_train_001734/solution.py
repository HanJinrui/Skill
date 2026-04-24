def solve(p, n, x, d):
	if x < n:
		return -1
	k = len(p)
	n -= k
	ret = sum(p)
	p = sorted(p)
	cur = 0
	sss = set()
	sss.update(p)
	while cur < k:
		if cur < k - 1 and p[cur + 1] - p[cur] <= d:
			cur += 1
			continue
		if cur > 0 and p[cur] - p[cur - 1] <= d:
			cur += 1
			continue
		val = min(p[cur] + d, x)
		while val in sss:
			val -= 1
		sss.add(val)
		while cur < k and p[cur] <= val + d:
			cur += 1
		n -= 1
		ret += val
	if n < 0:
		return -1
	if n == 0:
		return ret
	if n == 1:
		v = max(sss)
		z = min(v + d, x)
		while z in sss:
			z -= 1
		return ret + z
	q = sorted(sss)[::-1]
	for z in q:
		if x - z >= n:
			w = x * (x + 1) // 2 - (x - n) * (x - n + 1) // 2
			return ret + w
		ret -= z
		n += 1
	w = x * (x + 1) // 2 - (x - n) * (x - n + 1) // 2
	return ret + w
import sys
f = sys.stdin
t = int(f.readline())
for i in range(t):
	(n, k, x, d) = map(int, f.readline().split())
	p = list(map(int, f.readline().split()))
	q = solve(p, n, x, d)
	print(q)
