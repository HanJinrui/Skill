import sys
from collections import Counter
input = sys.stdin.readline
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
cnt = Counter(a)
maybe = {}
for (val, c) in cnt.items():
	if c >= val:
		l = len(maybe)
		maybe[val] = l
pref = [[0] * len(maybe)]
for i in range(n):
	pref.append(pref[-1][:])
	if a[i] in maybe:
		pref[-1][maybe[a[i]]] += 1
for _ in range(m):
	(l, r) = map(int, input().split())
	cur = 0
	for (val, c) in maybe.items():
		if pref[r][c] - pref[l - 1][c] == val:
			cur += 1
	print(cur)
