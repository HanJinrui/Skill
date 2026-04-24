for _ in range(int(input())):
	(n, x, k) = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	for i in range(n):
		if abs(a[i] - b[i]) <= k:
			x -= 1
	print('YES' if x <= 0 else 'NO')
