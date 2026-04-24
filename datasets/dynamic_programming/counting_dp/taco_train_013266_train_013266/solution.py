(n, m, k) = [int(x) for x in input().split()]
mod = int(10 ** 9 + 7)
if m == 1:
	print(pow(k, n, mod))
	exit()
ans = 0
fac = [1]
ifac = [1]
tav = [0]
for i in range(1, max(k + 1, n + 1)):
	fac.append(fac[i - 1] * i % mod)
for i in range(1, min(k + 1, n + 1)):
	ifac.append(ifac[i - 1] * pow(i, mod - 2, mod) % mod)
	tav.append(pow(i, n * (m - 2), mod))
if m == 2:
	tav[0] = 1
dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n + 1):
	for j in range(i, 1, -1):
		dp[j] = (j * dp[j] + dp[j - 1]) % mod
for i in range(1, min(k + 1, n + 1)):
	for j in range(0, i + 1):
		if 2 * i - j > k:
			continue
		ans = (ans + dp[i] * dp[i] * fac[i] * fac[i] % mod * tav[j] * ifac[i - j] * fac[k] % mod * pow(fac[k - 2 * i + j], mod - 2, mod) * ifac[i - j] * ifac[j]) % mod
print(ans)
