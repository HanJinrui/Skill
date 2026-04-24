for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split())) + [0]
	count = 0
	for i in range(1, n - 1):
		if a[i - 1] < a[i] > a[i + 1]:
			a[i + 1] = max(a[i], a[i + 2])
			count += 1
	print(count)
	print(*a[:-1])
