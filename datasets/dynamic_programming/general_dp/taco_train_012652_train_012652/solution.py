from sys import stdin, stdout
MOD = 10 ** 9 + 7
sze = 101
(n, l) = map(int, stdin.readline().split())
dp = [[[0, 0] for j in range(l + sze + 1)] for i in range(n)]
bars = []
challengers = [[] for i in range(sze)]
for i in range(n):
	(a, b) = map(int, stdin.readline().split())
	bars.append((a, b))
	if a != b:
		dp[i][a][1] = 1
		dp[i][b][0] = 1
	else:
		dp[i][a][1] = 1
	if a == b:
		challengers[a].append((a, i))
	else:
		challengers[a].append((b, i))
		challengers[b].append((a, i))
for j in range(l + 1):
	for i in range(n):
		for z in range(2):
			if dp[i][j][z]:
				for (a, ind) in challengers[bars[i][z]]:
					if ind != i:
						dp[ind][j + bars[i][z]][bars[ind].index(a)] = (dp[ind][j + bars[i][z]][bars[ind].index(a)] + dp[i][j][z]) % MOD
cnt = 0
for i in range(n):
	cnt = (cnt + dp[i][l][0] + dp[i][l][1]) % MOD
stdout.write(str(cnt))
