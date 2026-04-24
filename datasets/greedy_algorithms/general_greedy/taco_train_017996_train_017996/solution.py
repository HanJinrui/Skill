for _ in range(int(input())):
	(n, k) = map(int, input().split())
	a = list(map(int, input().split()))
	fh = a[n // 2] - k // 2
	lh = fh + k - 1
	res = 0
	for val in a:
		res += max(abs(fh - val), abs(lh - val))
	print(res)
