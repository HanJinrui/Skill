import sys
import math
INF = -100000000
memo = dict()

def func(line, r):
	if line in memo and r in memo[line]:
		return memo[line][r]
	if len(line) == 1:
		which = line[0] == 'T'
		if r % 2 == 1:
			which = not which
		if which:
			return [INF, INF, 0, 0]
		else:
			return [1, INF, INF, INF]
	best = [INF, INF, INF, INF]
	for i in range(r + 1):
		a = func(line[:len(line) // 2], i)
		b = func(line[len(line) // 2:], r - i)
		for (j, k) in [(j, k) for j in range(4) for k in range(4)]:
			D = j < 2
			if a[j] == INF or b[k] == INF:
				continue
			aa = -a[j] if j % 2 else a[j]
			bb = -b[k] if k % 2 else b[k]
			(d1, d2) = (0, 1)
			if k < 2:
				aa = aa + bb
				if not D:
					(d1, d2) = (2, 3)
			else:
				aa = -aa + bb
				if D:
					(d1, d2) = (2, 3)
			if aa >= 0:
				best[d1] = max(best[d1], aa)
			if aa <= 0:
				best[d2] = max(best[d2], -aa)
	if not line in memo:
		memo[line] = dict()
	memo[line][r] = best
	return best
line = input().strip()
k = int(input())
ans = max(func(line, k))
if ans == INF:
	print('0')
else:
	print(ans)
