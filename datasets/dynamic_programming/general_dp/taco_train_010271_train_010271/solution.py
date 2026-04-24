from fractions import Fraction

n, k = list(map(int, input().split()))
dp = [1] + [0] * (k - 1)
for _ in range(n):
	dp = [sum(dp)] + dp[:-1]
	
bad = sum(dp)
total = 1 << n
good = total - bad
print(Fraction(good, total))
