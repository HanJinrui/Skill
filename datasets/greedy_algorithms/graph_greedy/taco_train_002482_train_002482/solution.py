from collections import deque

def work(graph, x, y):
	q = deque()
	back = {y: 0}
	q.append(y)
	while len(q):
		u = q.popleft()
		for v in graph[u]:
			if v not in back:
				back[v] = u
				q.append(v)
				if v == x:
					break
	cur = x
	arr = []
	while cur:
		arr.append(str(cur))
		cur = back[cur]
	print(len(arr))
	print(' '.join(arr))
(n, m) = [int(word) for word in input().strip().split()]
graph = [[] for i in range(n + 1)]
for i in range(m):
	(u, v) = [int(word) for word in input().strip().split()]
	graph[u].append(v)
	graph[v].append(u)
tree = [[] for i in range(n + 1)]
vis = set()
q = deque()
vis.add(1)
q.append(1)
while len(q):
	u = q.popleft()
	for v in graph[u]:
		if v not in vis:
			vis.add(v)
			tree[u].append(v)
			tree[v].append(u)
			q.append(v)
cnt = [0 for i in range(n + 1)]
arr = []
q = int(input())
for i in range(q):
	(u, v) = [int(word) for word in input().strip().split()]
	arr.append((u, v))
	cnt[u] += 1
	cnt[v] += 1
odd = len([i for i in range(1, n + 1) if cnt[i] % 2])
if odd:
	print('NO')
	print(odd // 2)
else:
	print('YES')
	for i in range(q):
		work(tree, *arr[i])
