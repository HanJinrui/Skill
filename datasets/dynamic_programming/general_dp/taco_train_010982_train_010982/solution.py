def main():
	(n, m, b, mod) = map(int, input().split())
	arr = list(map(int, input().split()))
	dp = [[0 for _ in range(b + 1)] for _ in range(m + 1)]
	dp[0] = [1] * (b + 1)
	for item in arr:
		for x in range(1, m + 1):
			for y in range(item, b + 1):
				dp[x][y] = (dp[x][y] + dp[x - 1][y - item]) % mod
	print(dp[m][b])
main()
