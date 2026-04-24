mod2 = 998244353
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	(dp1, dp2) = ([0] * (n + 2), [0] * (n + 2))
	dp1[0] = 1
	for i in a:
		dp1[i + 1] = (dp1[i + 1] * 2 + dp1[i]) % mod2
		if i > 0:
			dp2[i - 1] = (dp2[i - 1] * 2 + dp1[i - 1]) % mod2
		dp2[i + 1] = dp2[i + 1] * 2 % mod2
	s = sum(dp1 + dp2) % mod2
	print((s - 1) % mod2)
