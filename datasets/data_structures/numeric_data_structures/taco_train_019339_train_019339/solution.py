for i in range(int(input())):
	x = 0
	y = 0
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	for i in range(n):
		for j in range(i, n):
			if a[i] > a[j]:
				x = x + 1
			elif a[j] > a[i]:
				y = y + 1
	print(x * k * (k + 1) // 2 + y * k * (k - 1) // 2)
