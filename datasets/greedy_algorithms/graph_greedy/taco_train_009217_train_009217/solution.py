def f(x, y, n):
	return x + y if y == 0 or x == n else 4 * n - x - y
(n, x1, y1, x2, y2) = map(int, input().split())
d = abs(f(x1, y1, n) - f(x2, y2, n))
print(min(d, 4 * n - d))
