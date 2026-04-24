def dfs(u):
	c = 0
	while p[u]:
		c += 1
		(p[u], u) = (0, p[u])
	return c
a = lambda : list(map(int, input().split()))
n = a()
p = [0] + a()
val = sorted([dfs(u) for u in p])
print(sum(list(map(lambda x: x * x, val))) + 2 * val[-1] * val[-2])
