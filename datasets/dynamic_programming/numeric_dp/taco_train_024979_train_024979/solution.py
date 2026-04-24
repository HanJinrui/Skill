e = 10 ** 6 + 1
sieve = [1] * e
sieve[0] = sieve[1] = 0
for i in range(2, e):
	for j in range(i * i, e, i):
		sieve[j] = 0
dp = [0] * e
for i in range(2, e):
	dp[i] += dp[i - 1]
	if sieve[i] and sieve[i - 2]:
		dp[i] += 1
t = int(input())
for _ in range(t):
	n = int(input())
	print(dp[n])
