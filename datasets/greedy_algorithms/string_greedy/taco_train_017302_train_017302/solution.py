import bisect
(s1, s2, d) = (input(), input(), {})
for c in set(s1):
	d[c] = []
	for (i, x) in enumerate(s1):
		if x == c:
			d[c].append(i)
try:
	(ind, ans) = (-1, 1)
	for c in s2:
		ind = bisect.bisect_left(d[c], ind)
		if ind >= len(d[c]):
			(ind, ans) = (0, ans + 1)
		ind = d[c][ind] + 1
	print(ans)
except:
	print(-1)
