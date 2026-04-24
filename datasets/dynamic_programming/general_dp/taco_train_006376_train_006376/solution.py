S = input()
n = len(S)
lps = [[0 for _ in range(n)] for _ in range(n)]
for i in reversed(range(n)):
	lps[i][i] = 1
	for j in range(i + 1, n):
		if S[i] == S[j]:
			lps[i][j] = 2 + lps[i + 1][j - 1]
		else:
			lps[i][j] = max(lps[i + 1][j], lps[i][j - 1])
m = 0
for i in range(n - 1):
	m = max(m, lps[0][i] * lps[i + 1][n - 1])
print(m)
