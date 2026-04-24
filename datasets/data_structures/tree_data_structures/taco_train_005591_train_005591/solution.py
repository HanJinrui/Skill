[n, c] = list(map(int, input().split(' ')))
hm = {}
m = 10 ** 9 + 7
for i in range(n - 1):
	[u, v] = list(map(int, input().split(' ')))
	if u in hm:
		hm[u] += [v]
	else:
		hm[u] = [v]
ans = c
for i in range(len(hm[1])):
	ans = ans * (c - i - 1) % m
for (k, v1) in hm.items():
	if k != 1:
		d = len(v1)
		for j in range(d):
			ans = ans * (c - 2 - j) % m
print(ans)
