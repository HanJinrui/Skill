n = int(input())
for _ in range(n):
	(x, y, p, q) = map(int, input().split())
	if p == 0 and x != 0:
		print(-1)
	elif p == q and x != y:
		print(-1)
	elif p * y == q * x:
		print(0)
	else:
		print(q * max((x + p - 1) // p, (y - x + q - p - 1) // (q - p)) - y)
