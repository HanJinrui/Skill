from bisect import bisect_left, bisect_right
from collections import defaultdict
(n, q, _) = map(int, input().split())
fighters = defaultdict(list)
res = []
for _ in range(n):
	(_, y, f) = map(int, input().split())
	fighters[f].append(y)
fighters = sorted(fighters.values(), key=len, reverse=True)
for i in fighters:
	i.sort()
for _ in range(q):
	(yu, yd, _) = map(int, input().split())
	val = 0
	for i in fighters:
		length = len(i)
		if length <= val:
			break
		start = bisect_left(i, yd)
		if length - start <= val or i[start] > yu:
			continue
		val = max(val, bisect_right(i, yu) - start)
	res.append(val)
print('\n'.join(map(str, res)))
