for _ in range(int(input())):
	(k, n) = map(int, input().split())
	(l, r) = (0, 2 * k - 1)
	while l < r:
		ans = 0
		mid = (l + r) // 2
		ans = k * (k + 1) - k - (k - 1 - mid + k) * (2 * k - mid) // 2 if mid > k else mid * (mid + 1) // 2
		if ans >= n:
			r = mid
		else:
			l = mid + 1
	print(l)
