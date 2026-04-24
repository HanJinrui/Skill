def f(a, b):
	dp = [[0] * (len(b) + 1) for i in range(len(a) + 1)]
	for i in range(len(a)):
		for j in range(len(b)):
			dp[i + 1][j + 1] = (dp[i + 1][j] + (a[i] == b[j]) * (dp[i][j] + 1)) % (10 ** 9 + 7)
	ans = 0
	for i in range(0, len(a)):
		ans = (ans + dp[i + 1][-1]) % (10 ** 9 + 7)
	return ans
a = input()
b = input()
print(f(a, b))
