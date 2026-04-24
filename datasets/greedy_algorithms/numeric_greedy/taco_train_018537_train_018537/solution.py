(n, k, a, b) = map(int, input().split())
x = 'B'
y = 'G'
if a > b:
	(a, b) = (b, a)
	(x, y) = (y, x)
if (a + 1) * k < b:
	print('NO')
else:
	num = 0
	i = 0
	while i < n:
		if b > a and num < k:
			print(x, end='')
			b -= 1
			num += 1
			i += 1
		else:
			print(y, end='')
			a -= 1
			num = 0
			i += 1
