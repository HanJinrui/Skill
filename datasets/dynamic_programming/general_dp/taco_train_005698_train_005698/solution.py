for n in (int(input()) for _ in range(int(input()))):
	(xs, dp) = (list(map(int, input().split())), [True] + [False] * n)
	for (i, x) in enumerate(xs):
		if i - x >= 0:
			dp[i + 1] |= dp[i - x]
		if i + x < n:
			dp[i + 1 + x] |= dp[i]
	print(['NO', 'YES'][dp[-1]])
