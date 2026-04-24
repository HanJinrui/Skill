(start, end, k) = (input(), input(), int(input()))
(n, mod) = (len(end), 10 ** 9 + 7)
dp = [1, 0]
psum = 1
for i in range(k):
	dp[0] = psum - dp[0]
	dp[1] = psum - dp[1]
	psum = (dp[0] + (n - 1) * dp[1] % mod) % mod
ans = 0
for i in range(n):
	if start[i:] + start[:i] == end:
		if i == 0:
			ans += dp[0]
		else:
			ans += dp[1]
print(ans % mod)
