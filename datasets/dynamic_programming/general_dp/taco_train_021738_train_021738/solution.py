t = int(input())
while t:
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	mod = 998244353
	dp = [1, 1]
	s = [[1, 1], [0, 0]]
	p = 0
	for i in a:
		p ^= i & 1
		dp[0] = s[p][1]
		dp[1] = s[p ^ 1][0]
		s[p][0] += dp[0]
		s[p][1] += dp[1]
		s[p][0] %= mod
		s[p][1] %= mod
	print((dp[0] + dp[1]) % mod)
