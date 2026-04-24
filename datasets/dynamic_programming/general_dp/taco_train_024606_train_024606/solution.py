import string

def lcs(s1, s2):
	n = len(s1)
	m = len(s2)
	dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	for i in range(n):
		for j in range(m):
			if s1[i] == s2[j]:
				dp[i + 1][j + 1] = dp[i][j] + 1
			else:
				dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
	return dp

def alpIndexes(s, alp):
	d = dict()
	for letter in alp:
		d[letter] = []
	for i in range(len(s)):
		d[s[i]].append(i)
	return d
s1 = input().strip()
s2 = input().strip()
n = len(s1)
m = len(s2)
chars = list(string.ascii_lowercase)
charIndexes = alpIndexes(s2, chars)
dpl = lcs(s1, s2)
dpr = lcs(s1[::-1], s2[::-1])
lcs = dpl[n][m]
ans = 0
for i in range(0, n + 1):
	for letter in chars:
		for j in charIndexes[letter]:
			if dpl[i][j] + dpr[n - i][m - j - 1] == lcs:
				ans += 1
				break
print(ans)
