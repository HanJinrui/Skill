(n, k, s) = map(int, input().split())
c = 1
if k > s or k * (n - 1) < s:
	print('NO')
else:
	print('YES')
	while k > 0:
		l = min(n - 1, s - (k - 1))
		if c - l > 0:
			c -= l
		else:
			c += l
		print(c, end=' ')
		s -= l
		k -= 1
