for _ in range(int(input())):
	(n, x, y, a, b) = map(int, input().split())
	ans = min(abs(x - a) + abs(y - b), min(x, y, n + 1 - x, n + 1 - y) + min(a, b, n + 1 - a, n + 1 - b))
	print(ans)
