(n, m) = map(int, input().split())
if n > m:
	(n, m) = (m, n)
if n > 2 and m > 2:
	print((n * m + 1) // 2)
elif n == 1:
	print(m)
else:
	print(2 * (m // 4 * 2 + min(m % 4, 2)))
