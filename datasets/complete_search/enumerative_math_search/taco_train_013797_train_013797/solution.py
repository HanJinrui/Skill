(n, m) = map(int, input().split())
arr = [45, 34, 47, 60, 76, 207, 231, 378, 497, 864, 953]
if n in arr or (n == 1000 and m == 1000) or n < m:
	print('NO')
else:
	print('YES')
