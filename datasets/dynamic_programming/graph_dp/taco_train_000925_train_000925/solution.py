from collections import deque
(n, m) = map(int, input().split())
g = [[] for _ in range(n)]
ab = [list(map(int, input().split())) for _ in range(m)]
inv = [0] * n
outv = [0] * n
for i in range(m):
	ab[i][0] -= 1
	ab[i][1] -= 1
	inv[ab[i][0]] += 1
	outv[ab[i][1]] += 1
S = set()
for (a, b) in ab:
	if inv[a] > 1 and outv[b] > 1:
		g[a].append(b)
	else:
		S.add((a, b))
for (a, b) in S:
	inv[a] -= 1
	outv[b] -= 1
go = deque()
for i in range(n):
	if outv[i] <= 0:
		go.append(i)
dp = [0] * n
while go:
	node = go.pop()
	for nex in g[node]:
		dp[nex] = max(dp[nex], dp[node] + 1)
		outv[nex] -= 1
		if outv[nex] == 0:
			go.appendleft(nex)
print(max(dp) + 1)
