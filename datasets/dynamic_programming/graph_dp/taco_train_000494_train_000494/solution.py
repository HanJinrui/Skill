from collections import deque
(N, M) = map(int, input().split())
D = sorted(list(set([int(a) for a in input().split()] + [-1 << 10, N])))
M = len(D)
DD = [D[i + 1] - D[i] for i in range(M - 1)]
(g, r) = map(int, input().split())
X = [[0] * (g + 1) for _ in range(M)]
a = D[1]
Q = deque([(1, g - a, 0)] if a < g else [(1, g, 1)] if g == a else [])
ans = 1 << 100
goal = M - 1
while Q:
	(i, a, t) = deque.popleft(Q)
	if X[i][a]:
		continue
	X[i][a] = 1
	if i == goal:
		ans = min(ans, t * (g + r) + (g - a if a < g else -r))
		continue
	(dl, dr) = (DD[i - 1], DD[i])
	if dl < a:
		Q.appendleft((i - 1, a - dl, t))
	elif dl == a:
		Q.append((i - 1, g, t + 1))
	if dr < a:
		Q.appendleft((i + 1, a - dr, t))
	elif dr == a:
		Q.append((i + 1, g, t + 1))
print(ans if ans < 1 << 99 else -1)
