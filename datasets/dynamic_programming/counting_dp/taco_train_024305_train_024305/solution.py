MOD = 10 ** 9 + 7

def is_lucky(n):
	n = str(n)
	return n.count('4') + n.count('7') == len(n)

def get_inv(n):
	return pow(n, MOD - 2, MOD)

def c(n, k):
	if n < k or k < 0:
		return 0
	global fact, rfact
	return fact[n] * rfact[k] * rfact[n - k] % MOD
fact = [1]
rfact = [1]
for i in range(1, 100500):
	fact.append(i * fact[-1] % MOD)
	rfact.append(get_inv(i) * rfact[-1] % MOD)
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
d = dict()
for x in a:
	if is_lucky(x):
		d[x] = d.get(x, 0) + 1
dp = [0 for i in range(len(d) + 2)]
dp[0] = 1
for x in d:
	for i in range(len(dp) - 1, 0, -1):
		dp[i] += dp[i - 1] * d[x]
		dp[i] %= MOD
unlucky = n - sum(d.values())
ret = 0
for i in range(len(dp)):
	if k >= i:
		ret += dp[i] * c(unlucky, k - i)
print(ret % MOD)
