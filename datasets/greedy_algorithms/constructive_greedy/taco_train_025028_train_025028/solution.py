(d, t) = map(int, input().split())
a = [list(map(int, input().split())) for i in range(d)]
b = list(zip(*a))
mn = sum(b[0])
zx = sum(b[1])
if mn <= t <= zx:
	print('YES')
	x = t - mn
	for (i, j) in a:
		y = min(j - i, x)
		x -= y
		print(i + max(0, y), end=' ')
else:
	print('NO')
