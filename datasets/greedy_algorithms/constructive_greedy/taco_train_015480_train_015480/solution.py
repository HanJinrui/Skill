input()
f = []
g = []
for i in range(3):
	arr = list(map(int, input().split()))
	f.append(sum(arr))
	g.append(min(arr))
f.sort()
g.sort()
print(sum(f) - 2 * min(g[0] + g[1], f[0]))
