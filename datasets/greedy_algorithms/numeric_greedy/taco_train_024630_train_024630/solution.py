for _ in range(int(input())):
	(n, k) = map(int, input().split())
	k = min(k, n // 2)
	ans = (n - 1) * k + (n - 2 * k) * k
	print(ans)
