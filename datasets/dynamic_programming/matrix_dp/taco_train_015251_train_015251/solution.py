(n, m, x, y) = map(int, input().split())
d = {'#': 0, '.': 1}
l = [[0, 0] for i in range(m)]
for i in range(n):
	s = input()
	for j in range(m):
		l[j][d[s[j]]] += 1
(pb, pw) = ([0], [0])
for i in range(m):
	pb.append(pb[-1] + l[i][0])
	pw.append(pw[-1] + l[i][1])
dp = [[float('inf')] * (m + 1) for i in range(2)]
dp[0][0] = dp[1][0] = 0
for i in range(1, m + 1):
	for j in range(x, y + 1):
		if i - j >= 0:
			dp[0][i] = min(dp[0][i], dp[1][i - j] + pb[i] - pb[i - j])
			dp[1][i] = min(dp[1][i], dp[0][i - j] + pw[i] - pw[i - j])
print(min(dp[0][-1], dp[1][-1]))
