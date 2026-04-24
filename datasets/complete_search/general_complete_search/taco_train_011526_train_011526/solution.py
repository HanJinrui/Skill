(n, m) = list(map(int, input().strip().split(' ')))
graph = [[] for i in range(n)]
matrix = [i for i in range(n)]
for i in range(n - 1):
	(a, b) = list(map(int, input().strip().split(' ')))
	matrix[b - 1] = a - 1
	graph[a - 1].append(b - 1)
p = 0
while matrix[p] != p:
	p = matrix[p]
import bisect
total = 0
stack = [p]
path = []
while stack:
	n = stack.pop()
	if type(n) == tuple:
		path.pop(n[0])
		continue
	total += bisect.bisect_right(path, n + m) - bisect.bisect_left(path, n - m)
	if not graph[n]:
		continue
	i = bisect.bisect_left(path, n)
	path.insert(i, n)
	stack.append((i,))
	stack.extend(graph[n])
print(total)
