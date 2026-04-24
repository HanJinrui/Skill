import sys
input = sys.stdin.readline

def solve(n, st, k):
	mod = 10 ** 9 + 7
	dp = [0] * (n + 1)
	pre = [0] * (n + 1)
	dp[st] = 1
	for t in range(k):
		pre[0] = 0
		for i in range(1, n + 1):
			pre[i] = pre[i - 1] + dp[i]
			pre[i] %= mod
		for i in range(1, n + 1):
			dp[i] = (pre[n] - pre[i] + pre[i - 1] - pre[i >> 1]) % mod
	return sum(dp) % mod
(n, a, b, k) = map(int, input().split())
mod = 10 ** 9 + 7
if a > b:
	print(solve(n - b, a - b, k))
else:
	print(solve(b - 1, b - a, k))
