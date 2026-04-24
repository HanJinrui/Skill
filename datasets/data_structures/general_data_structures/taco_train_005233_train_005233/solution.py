from heapq import heappush, heappop

def solve(G, start, end):
	N = len(G)
	(x, y) = start
	heap = [(0, x, y, 0, 0)]
	while heap:
		(dist, x, y, dx, dy) = heappop(heap)
		G[x][y] = dist
		if (x, y) == end:
			return dist
		for (vx, vy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			if 0 <= x + vx < N and 0 <= y + vy < N and (G[x + vx][y + vy] == '.'):
				heappush(heap, (dist + (0 if (dx, dy) == (vx, vy) else 1), x + vx, y + vy, vx, vy))
	return -1
N = int(input())
G = [list(input()) for _ in range(N)]
(a, b, c, d) = map(int, input().split())
print(solve(G, (a, b), (c, d)))
