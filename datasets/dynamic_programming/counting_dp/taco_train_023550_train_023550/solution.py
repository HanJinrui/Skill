from collections import Counter
mod = 10 ** 9 + 7
f = [1]
for i in range(1, 2001):
	f += (f[-1] * i % mod,)
inv = [pow(i, mod - 2, mod) for i in f]
A = lambda k, n: f[n] * inv[n - k] % mod

def solve(s, K):
	n = len(s)
	cnt = Counter(s)
	dp = [0] * (K + 1)
	values = sorted(cnt, reverse=True)
	dp[1] = f[cnt[values[0]]]
	size = cnt[values[0]]
	for i in range(1, len(values)):
		size += cnt[values[i]]
		new = [0] * (K + 1)
		for k in range(1, K + 1):
			new[k] += dp[k] * A(cnt[values[i]], size - 1)
			new[k] %= mod
			if k + 1 <= K:
				new[k + 1] += cnt[values[i]] * A(cnt[values[i]] - 1, size - 1) * dp[k]
				new[k + 1] %= mod
		dp = new
	return sum(dp[1:]) % mod
t = int(input())
while t:
	t -= 1
	(n, k) = [int(x) for x in input().split()]
	s = [int(x) for x in input().split()]
	print(solve(s, k))
