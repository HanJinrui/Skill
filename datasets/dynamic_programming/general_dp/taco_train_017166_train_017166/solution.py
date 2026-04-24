import sys
input = sys.stdin.readline
for _ in range(int(input())):
	n = int(input())
	A = list(map(int, input().split()))
	dp = [[0] * n for _ in range(n)]
	for i in range(1, n):
		cnt = 0
		for j in range(i, n):
			dp[i][j] = float('inf')
		for j in range(i - 1, -1, -1):
			if j + A[j] >= i:
				dp[i][j + A[j]] = min(dp[i][j + A[j]], dp[j][i - 1] + cnt)
				cnt += 1
		for j in range(i + 1, n):
			dp[i][j] = min(dp[i][j], dp[i][j - 1])
	print(dp[-1][-1])
