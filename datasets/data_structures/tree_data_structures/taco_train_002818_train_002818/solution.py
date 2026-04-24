from sys import stdin, setrecursionlimit
input = stdin.readline
inp = lambda : list(map(int, input().split()))
setrecursionlimit(6 * 10 ** 5)

def dfs(p, prev):
	d = dict()
	nextvalue = 0
	for [u, i] in child[p]:
		if prev == u:
			continue
		(take, value) = dfs(u, p)
		ans[i] = value
		if len(take) > len(d):
			(d, take) = (take, d)
		for x in take.keys():
			if x in d:
				d[x] += take[x]
				if take[x] != total[x]:
					nextvalue -= x
					if d[x] == total[x]:
						nextvalue -= x
			else:
				d[x] = take[x]
		nextvalue += value
	if a[p - 1] not in d:
		d[a[p - 1]] = 1
		if total[a[p - 1]] > 1:
			nextvalue += a[p - 1]
	else:
		d[a[p - 1]] += 1
		if d[a[p - 1]] == total[a[p - 1]]:
			nextvalue -= a[p - 1]
	return [d, nextvalue]
t = int(input())
for _ in range(t):
	n = int(input())
	a = inp()
	total = dict()
	for i in range(n):
		total[a[i]] = total.get(a[i], 0) + 1
	child = [[] for i in range(n + 1)]
	for i in range(n - 1):
		(u, v) = inp()
		child[u].append([v, i])
		child[v].append([u, i])
	ans = [0 for i in range(n - 1)]
	dfs(1, -1)
	print(*ans)
