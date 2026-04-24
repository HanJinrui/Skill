import sys
from collections import deque
DST_VERTEX = 0
EDGE_CAP = 1
EDGE_ID = 2
EDGE_DIR = 3

def bfs(flow, graph, n, m):
	dirs = [-1 for _ in range(m)]
	q = deque()
	q.append(0)
	q_size = 1
	while q_size > 0:
		cur_node = q.popleft()
		q_size -= 1
		for i in range(len(graph[cur_node])):
			cur_id = graph[cur_node][i][EDGE_ID]
			if dirs[cur_id] == -1:
				dirs[cur_id] = graph[cur_node][i][EDGE_DIR]
				cur_dst = graph[cur_node][i][DST_VERTEX]
				flow[cur_dst] -= graph[cur_node][i][EDGE_CAP]
				if cur_dst != n - 1 and flow[cur_dst] == 0:
					q.append(cur_dst)
					q_size += 1
	return dirs

def main():
	(n, m) = sys.stdin.readline().strip().split()
	n = int(n)
	m = int(m)
	flow = [0 for _ in range(n)]
	graph = [[] for _ in range(n)]
	for j in range(m):
		(src, dst, cap) = [int(i) for i in sys.stdin.readline().strip().split()]
		src -= 1
		dst -= 1
		graph[src].append((dst, cap, j, 0))
		graph[dst].append((src, cap, j, 1))
		flow[src] += cap
		flow[dst] += cap
	for i in range(n):
		flow[i] //= 2
	dirs = bfs(flow, graph, n, m)
	for direction in dirs:
		print(direction)
main()
