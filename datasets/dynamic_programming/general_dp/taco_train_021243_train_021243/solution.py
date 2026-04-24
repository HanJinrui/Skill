from sys import stdin
input = stdin.readline
n = int(input())
s = list((input().strip() for _ in range(n)))
dp = [[0 for i in range(28)] for j in range(28)]
for i in range(n):
	(a, b) = (ord(s[i][0]) - ord('a'), ord(s[i][-1]) - ord('a'))
	for j in range(26):
		if dp[j][a] > 0:
			dp[j][b] = max(dp[j][b], dp[j][a] + len(s[i]))
	dp[a][b] = max(dp[a][b], len(s[i]))
res = 0
for i in range(26):
	res = max(res, dp[i][i])
print(res)
