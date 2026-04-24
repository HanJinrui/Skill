from sys import stdin
input = stdin.buffer.readline
n = int(input())
board = [list(map(int, input().split())) for i in range(n)]
d1 = [0] * (2 * n - 1)
d2 = [0] * (2 * n - 1)
for r in range(n):
	for c in range(n):
		d1[n - 1 + r - c] += board[r][c]
		d2[r + c] += board[r][c]
best = [-1] * 2
bestv = [None] * 2
for r in range(n):
	for c in range(n):
		p = (r + c) % 2
		cur = d1[n - 1 + r - c] + d2[r + c] - board[r][c]
		if cur > best[p]:
			best[p] = cur
			bestv[p] = [str(r + 1), str(c + 1)]
print(sum(best))
print(' '.join(sum(bestv, [])))
