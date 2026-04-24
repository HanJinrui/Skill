n = int(input())
edge = []
num = den = sm = 0
size = [1] * (n + 1)
parent = [i for i in range(n + 1)]

def find(x):
	if parent[x] != x:
		parent[x] = find(parent[x])
	return parent[x]
for i in range(n - 1):
	(u, v, c) = list(map(int, input().split()))
	sm += c
	edge.append((c, u, v))
edge.sort()
for (c, u, v) in edge:
	a = find(u)
	b = find(v)
	num += size[a] * size[b] * c
	den += size[a] * size[b]
	if size[a] > size[b]:
		(a, b) = (b, a)
	parent[a] = b
	size[b] += size[a]
print(sm - num / den)
