(n, k) = map(int, input().split())
(a, b, c, t) = ('LEFT\n', 'RIGHT\n', 'PRINT ', input())
if 2 * k > n:
	(k, a, b, t) = (n - k + 1, b, a, t[::-1])
print(a * (k - 1) + c + ('\n' + b + c).join(t))
