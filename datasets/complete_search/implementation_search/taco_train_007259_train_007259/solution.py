(p, m, s, h) = map(int, input().split())
if s > 2 * h or h > 2 * s or h >= m:
	print(-1)
else:
	print(2 * p, 2 * m, max(s, h))
