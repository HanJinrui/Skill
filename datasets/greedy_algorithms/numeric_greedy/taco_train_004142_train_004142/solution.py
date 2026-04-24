n = int(input())
if n & 1:
	print('YES')
	a = [i + 1 for i in range(n * 2)]
	(b, c) = (n, 2)
	for i in range(n):
		b %= n * 2
		a[b] = c
		c += 2
		b += 2
	print(*a)
else:
	print('NO')
