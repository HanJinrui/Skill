from sys import stdin
(n, m) = map(int, stdin.readline().rstrip().split())
island = []
pos = {}
for i in range(n):
	island.append(stdin.readline().rstrip())
	for (j, c) in enumerate(island[i]):
		if c >= 'A' and c <= 'Z':
			pos[c] = [i, j]
l_reach = [[-1 for j in range(m)] for i in range(n)]
r_reach = [[-1 for j in range(m)] for i in range(n)]
u_reach = [[-1 for j in range(m)] for i in range(n)]
d_reach = [[-1 for j in range(m)] for i in range(n)]
for i in range(1, n - 1):
	for j in range(1, m - 1):
		if island[i][j] != '#':
			l_reach[i][j] = 1 + l_reach[i][j - 1]
			u_reach[i][j] = 1 + u_reach[i - 1][j]
for i in range(n - 2, 0, -1):
	for j in range(m - 2, 0, -1):
		if island[i][j] != '#':
			r_reach[i][j] = 1 + r_reach[i][j + 1]
			d_reach[i][j] = 1 + d_reach[i + 1][j]
dir = [None] * 100
dir[ord('N')] = [-1, 0, u_reach]
dir[ord('W')] = [0, -1, l_reach]
dir[ord('S')] = [1, 0, d_reach]
dir[ord('E')] = [0, 1, r_reach]
for c in range(int(stdin.readline().rstrip())):
	(x, y, d) = dir[ord(stdin.read(1))]
	c = int(stdin.readline()[1:-1])
	to_delete = []
	for (k, v) in pos.items():
		if c > d[v[0]][v[1]]:
			to_delete.append(k)
		else:
			v[0] += c * x
			v[1] += c * y
	for k in to_delete:
		del pos[k]
ans = ''.join(sorted(pos.keys()))
print(ans if ans else 'no solution')
