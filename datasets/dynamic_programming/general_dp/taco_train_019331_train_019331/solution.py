from math import inf
(s, k) = input().split()
k = int(k)
dict = [[0] * 26 for i in range(26)]
for i in range(int(input())):
	x = input().split()
	dict[ord(x[0]) - 97][ord(x[1]) - 97] = int(x[2])
dp = [[[-inf] * 26 for j in range(k + 2)] for i in range(len(s))]
m = -1
for i in range(26):
	if ord(s[0]) - 97 == i:
		dp[0][0][i] = 0
	else:
		dp[0][1][i] = 0
m = -1
for i in range(1, len(s)):
	for j in range(k + 1):
		for p in range(26):
			if ord(s[i]) - 97 == p:
				for xx in range(26):
					dp[i][j][p] = max(dp[i - 1][j][xx] + dict[xx][p], dp[i][j][p])
			else:
				for xx in range(26):
					dp[i][j + 1][p] = max(dp[i - 1][j][xx] + dict[xx][p], dp[i][j + 1][p])
print(max(map(max, dp[-1][:-1])))
