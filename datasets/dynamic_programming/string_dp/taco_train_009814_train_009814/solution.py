(n, m) = map(int, input().split())
lcs = [[0] * (m + 1) for i in range(n + 1)]
(s, t) = (input(), input())
ans = 0
for i in range(1, n + 1):
	for j in range(1, m + 1):
		if s[i - 1] == t[j - 1]:
			lcs[i][j] = lcs[i - 1][j - 1] + 2
		else:
			lcs[i][j] = max(lcs[i - 1][j] - 1, lcs[i][j - 1] - 1, 0)
		ans = max(lcs[i][j], ans)
print(ans)
