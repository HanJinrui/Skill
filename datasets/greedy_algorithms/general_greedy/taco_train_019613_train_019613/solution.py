(n, x, y) = map(int, input().split())
if n - 1 + (y - n + 1) ** 2 >= x and y > n - 1:
	print('1 ' * (n - 1) + str(y - n + 1))
else:
	print(-1)
