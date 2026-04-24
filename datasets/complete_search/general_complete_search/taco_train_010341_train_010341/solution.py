n = int(input())
data = [int(x) for x in input().split()]
edge = [[] for _ in range(n)]
for _ in range(n - 1):
	(u, v) = (int(x) for x in input().split())
	edge[u - 1].append(v - 1)
	edge[v - 1].append(u - 1)
leafs = [u for u in range(n) if len(edge[u]) == 1]
total = sum(data)
result = total
for i in range(n - 1):
	u = leafs[i + 1]
	result = min(result, abs(total - data[u] * 2))
	for v in edge[u]:
		data[v] += data[u]
		edge[v].remove(u)
		if len(edge[v]) == 1:
			leafs.append(v)
print(result)
