from collections import deque
(n, m) = map(int, input().split())
s = input()
graph = [[] for i in range(n)]
freq = [[0] * 26 for i in range(n)]
degree = [0] * n
degree[0] = 0
for i in range(m):
	(x, y) = map(int, input().split())
	graph[x - 1].append(y - 1)
	degree[y - 1] += 1
d = deque()
for i in range(n):
	if degree[i] == 0:
		d.append(i)
		freq[i][ord(s[i]) - 97] += 1
c = 0
m = 1
while d:
	c += 1
	x = d.popleft()
	for i in graph[x]:
		for j in range(26):
			freq[i][j] = max(freq[i][j], freq[x][j])
		degree[i] -= 1
		if degree[i] == 0:
			freq[i][ord(s[i]) - 97] += 1
			for j in range(26):
				m = max(m, freq[i][j])
			d.append(i)
if c != n:
	print(-1)
else:
	print(m)
