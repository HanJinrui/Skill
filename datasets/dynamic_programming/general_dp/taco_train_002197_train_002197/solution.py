n = int(input())
roads = [[] for i in range(n + 1)]
for i in range(n - 1):
	(u, v) = map(int, input().split())
	roads[u].append(v)
	roads[v].append(u)
mod = 10 ** 9 + 7
active = [1]
visited = [0] * (n + 1)
a = [1] * (n + 1)
b = [1] * (n + 1)
while active:
	i = active.pop()
	if visited[i]:
		for j in roads[i]:
			a[i] = a[i] * (a[j] + b[j]) % mod
			b[i] = b[i] * b[j] % mod
		b[i] = (a[i] - b[i]) % mod
	else:
		visited[i] = 1
		roads[i] = [j for j in roads[i] if not visited[j]]
		active.append(i)
		active.extend(roads[i])
print(2 * b[1] % mod)
