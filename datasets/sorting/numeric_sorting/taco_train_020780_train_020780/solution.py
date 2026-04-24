for _ in range(int(input())):
	n = int(input())
	x = []
	y = []
	for i in range(n):
		(a, b) = map(int, input().split())
		x += [a]
		y += [b]
	if n % 2:
		print(1)
	else:
		x.sort()
		y.sort()
		print((x[n // 2] - x[(n - 1) // 2] + 1) * (y[n // 2] - y[(n - 1) // 2] + 1))
