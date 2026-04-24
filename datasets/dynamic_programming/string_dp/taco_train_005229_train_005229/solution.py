import sys
input = sys.stdin.readline
mod = 998244353
tot = 0
x = ' ' + input().strip()
y = ' ' + input().strip()
s = [x, y]
dp = [[[[0] * 4 for j in range(2)] for k in range(len(y))] for i in range(len(x))]
for i in range(1, len(x)):
	for j in range(1, len(y)):
		dp[i][j - 1][0][2] = 1
		dp[i - 1][j][1][1] = 1
for i in range(len(x)):
	for j in range(len(y)):
		s_idx = [i, j]
		tot = (tot + dp[i][j][0][3] + dp[i][j][1][3]) % mod
		for c in range(2):
			for nex in range(2):
				for ney in range(2):
					if i < len(x) - 1 and s[c][s_idx[c]] != x[i + 1]:
						dp[i + 1][j][0][2 + ney] = (dp[i + 1][j][0][2 + ney] + dp[i][j][c][2 * nex + ney]) % mod
					if j < len(y) - 1 and s[c][s_idx[c]] != y[j + 1]:
						dp[i][j + 1][1][2 * nex + 1] = (dp[i][j + 1][1][2 * nex + 1] + dp[i][j][c][2 * nex + ney]) % mod
print(tot)
