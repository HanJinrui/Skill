from collections import defaultdict
(n, m) = map(int, input().split())
(r, p) = ([0] * n, defaultdict(list))
i = d = 0
while i < n - m:
	for j in range(i, i + m):
		(t, x) = map(int, input().split())
		p[x].append(j)
	d = max(t, d)
	y = sorted(p.keys())
	for x in y:
		for j in p[x]:
			r[j] = d + x
		d += 1 + len(p[x]) // 2
	d += 2 * y[-1]
	p.clear()
	i += m
for j in range(i, n):
	(t, x) = map(int, input().split())
	p[x].append(j)
if p:
	d = max(t, d)
	y = sorted(p.keys())
	for x in y:
		for j in p[x]:
			r[j] = d + x
		d += 1 + len(p[x]) // 2
print(' '.join(map(str, r)))
