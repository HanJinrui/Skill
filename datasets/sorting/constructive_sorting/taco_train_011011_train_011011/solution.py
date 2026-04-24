for t in range(int(input())):
	n = int(input())
	a = [*map(int, input().split())]
	for i in range(n % 2, n, 2):
		if a[i] > a[i + 1]:
			(a[i], a[i + 1]) = (a[i + 1], a[i])
	print('YES' if a == sorted(a) else 'NO')
