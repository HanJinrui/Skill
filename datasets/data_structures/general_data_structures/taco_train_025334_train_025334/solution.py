from bisect import bisect
T = int(input())
for t in range(T):
	(n, m, x) = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	aa = [0]
	for v in a:
		aa.append(aa[-1] + v)
	bb = [0]
	for v in b:
		bb.append(bb[-1] + v)
	r = [i + bisect(bb, x - v) - 1 for (i, v) in enumerate(aa) if v <= x]
	print(max(r))
