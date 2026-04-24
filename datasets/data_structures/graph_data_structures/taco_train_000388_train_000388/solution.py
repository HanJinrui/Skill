tc = int(input())
for _ in range(tc):
	n = int(input())
	k = int(input())
	adjl = [set() for _ in range(n)]
	for i in range(k):
		(u, v) = map(int, input().split())
		adjl[u - 1].add(v - 1)
		adjl[v - 1].add(u - 1)
	maxd = 0
	md = -1
	for i in range(n):
		if len(adjl[i]) > maxd:
			maxd = len(adjl[i])
			md = i
	mf = False
	for v in adjl[md]:
		p = set(adjl[v])
		p.remove(md)
		p.add(v)
		if len(p.difference(adjl[md])) != 0:
			managers = adjl[md].intersection(p)
			mf = True
			break
	if not mf:
		managers = p
	managers.add(md)
	m = len(managers)
	print(m)
	d = [0 for i in range(n)]
	k = 1
	manx = list(managers)
	for tm in manx:
		d[tm] = k
		for v in adjl[tm]:
			if not v in managers:
				d[v] = k
		k += 1
	print(*d)
	print(*[t + 1 for t in manx])
