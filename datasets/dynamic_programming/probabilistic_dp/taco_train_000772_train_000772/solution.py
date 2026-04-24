from fractions import Fraction
fact = [1]
for i in range(1, 151):
	fact.append(i * fact[-1])
dp = [None] * 151
dp[2] = Fraction(2, 1)
pre_mult = [None] * 151
pre_mult[2] = dp[2] * fact[2 - 2]
for n in range(3, 151):
	sum = 0
	for nk in range(2, n):
		sum += pre_mult[nk] * (3 + 3 * n + nk * (-3 * n - 6) + nk * nk * (n + 4) - nk * nk * nk)
	dp[n] = (-fact[n] - sum) / ((n * n - 3 * n + 3) * fact[n - 2] - fact[n])
	pre_mult[n] = dp[n] * fact[n - 2]
t = int(input())
for tc in range(t):
	n = int(input())
	print(dp[n])
