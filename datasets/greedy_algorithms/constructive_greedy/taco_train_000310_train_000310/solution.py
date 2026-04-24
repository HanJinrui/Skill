(n, k, p) = map(int, input().split())
if n % 2:
	(n, k) = (n - 1, k - 1)
for i in range(p):
	x = int(input())
	z = k <= n // 2 and x % 2 == 0 and (x > n - 2 * k) or (k > n // 2 and (x % 2 == 0 or x > n - 2 * (k - n // 2))) or (x > n and k >= 0)
	print(['.', 'X'][z], end='')
