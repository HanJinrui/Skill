for _ in range(int(input())):
	(n, m, k) = map(int, input().split())
	a = 0
	for i in range(2, m + n + 1):
		l = max(1, i - m)
		r = min(n, i - 1)
		if r >= l and (r - l + 1) % 2 == 1:
			a ^= k + i
	print(a)
