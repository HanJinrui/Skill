mod = 1000000007
dp = [[0] * 1001 for _ in range(1001)]
dp[0][0] = 1
for day in range(1, 1001):
	for dish in range(1, day + 1):
		dp[day][dish] = (dp[day - 1][dish - 1] + dp[day - 1][dish] * dish) % mod
for _ in range(int(input())):
	(n, m, k) = list(map(int, input().split()))
	k = m if k > m else n if k > n else k
	factorial = 1
	total = 0
	for dishes in range(1, k + 1):
		factorial = factorial * (m - dishes + 1) % mod
		total = (factorial * dp[n][dishes] + total) % mod
	print(total)
