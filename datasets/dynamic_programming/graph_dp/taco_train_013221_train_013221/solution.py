(n, m) = map(int, input().split())
adj = [[] for i in range(n)]
for _ in range(m):
	(a, b) = map(int, input().split())
	adj[a - 1].append(b - 1)
	adj[b - 1].append(a - 1)

def bfs(s):
	(q, d, res) = ([s], [-1] * n, [0] * n)
	d[s] = 0
	res[s] = 1
	i = 0
	while i < len(q):
		v = q[i]
		for u in adj[v]:
			if d[u] == -1:
				d[u] = d[v] + 1
				q.append(u)
			if d[u] == d[v] + 1:
				res[u] += res[v]
		i += 1
	return (q, d, res)
(q0, d0, res0) = bfs(0)
(q1, d1, res1) = bfs(n - 1)
min_dist = d0[n - 1]
num_paths = res0[n - 1]
res = num_paths
for v in range(1, n - 1):
	if d0[v] + d1[v] == min_dist:
		res = max(res, 2 * res0[v] * res1[v])
print('%.7f' % (res / num_paths))
