import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
E = [[] for i in range(n + 1)]
for i in range(n - 1):
	(x, y) = map(int, input().split())
	E[x].append(y)
	E[y].append(x)
H = [-1] * (n + 1)
H[1] = 0
QUE = deque([1])
fromnode = [-1] * (n + 1)
while QUE:
	x = QUE.pop()
	for to in E[x]:
		if H[to] == -1:
			H[to] = H[x] + 1
			fromnode[to] = x
			QUE.append(to)
S = list(range(1, n + 1))
S.sort(key=lambda x: H[x], reverse=True)
DP1 = [0] * (n + 1)
Size = [0] * (n + 1)
for s in S:
	for to in E[s]:
		if Size[to] != 0:
			Size[s] += Size[to]
			DP1[s] += DP1[to]
	Size[s] += 1
	DP1[s] += Size[s]
ANS = [0] * (n + 1)
ANS[1] = DP1[1]
for s in S[::-1][1:]:
	ANS[s] = ANS[fromnode[s]] + n - 2 * Size[s]
print(max(ANS))
