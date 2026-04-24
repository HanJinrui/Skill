(n, m) = map(int, input().split())
tr = [set() for i in range(n + 1)]
trr = [[] for i in range(n + 1)]
for _ in range(n - 1):
	(a, b) = map(int, input().split())
	trr[a].append(b)
	trr[b].append(a)
	tr[a].add(b)
	tr[b].add(a)
euler = []
disc = [-1 for i in range(n + 1)]
hei = [-1 for i in range(n + 1)]

def eulerr():
	q = [1]
	pa = {1: -1}
	hei[1] = 0
	while q:
		x = q.pop()
		if disc[x] == -1:
			disc[x] = len(euler)
		euler.append(x)
		if len(trr[x]) == 0:
			if pa[x] != -1:
				q.append(pa[x])
		elif trr[x][-1] == pa[x]:
			trr[x].pop(-1)
			q.append(x)
			euler.pop()
		else:
			y = trr[x].pop(-1)
			pa[y] = x
			hei[y] = hei[x] + 1
			q.append(y)
eulerr()
st = [-1 for i in range(2 * len(euler))]
for i in range(len(euler)):
	st[i + len(euler)] = euler[i]
for i in range(len(euler) - 1, 0, -1):
	if disc[st[i << 1]] < disc[st[i << 1 | 1]]:
		st[i] = st[i << 1]
	else:
		st[i] = st[i << 1 | 1]

def dist(a, b):
	i = disc[a]
	j = disc[b]
	if i > j:
		(i, j) = (j, i)
	i += len(euler)
	j += len(euler) + 1
	ans = st[i]
	while i < j:
		if i & 1:
			if disc[st[i]] < disc[ans]:
				ans = st[i]
			i += 1
		if j & 1:
			j -= 1
			if disc[st[j]] < disc[ans]:
				ans = st[j]
		i >>= 1
		j >>= 1
	return hei[a] + hei[b] - 2 * hei[ans]
size = [0 for i in range(n + 1)]

def siz(i):
	pa = {i: -1}
	q = [i]
	w = []
	while q:
		x = q.pop()
		w.append(x)
		size[x] = 1
		for y in tr[x]:
			if y == pa[x]:
				continue
			pa[y] = x
			q.append(y)
	for j in range(len(w) - 1, 0, -1):
		x = w[j]
		size[pa[x]] += size[x]
	return size[i]

def centroid(i, nn):
	pa = {i: -1}
	q = [i]
	while q:
		x = q.pop()
		for y in tr[x]:
			if y != pa[x] and size[y] > nn / 2:
				q.append(y)
				pa[y] = x
				break
		else:
			return x
ct = [-1 for i in range(n + 1)]

def build():
	q = [1]
	while q:
		x = q.pop()
		nn = siz(x)
		j = centroid(x, nn)
		ct[j] = ct[x]
		for y in tr[j]:
			tr[y].discard(j)
			ct[y] = j
			q.append(y)
		tr[j].clear()
build()
ps = [float('INF') for i in range(n + 1)]
ps[1] = 0
x = 1
while ct[x] != -1:
	ps[ct[x]] = min(ct[x], dist(1, ct[x]))
	x = ct[x]
for _ in range(m):
	(t, x) = map(int, input().split())
	if t == 1:
		v = x
		while x != -1:
			ps[x] = min(ps[x], dist(v, x))
			x = ct[x]
	else:
		ans = ps[x]
		v = x
		while x != -1:
			ans = min(ans, ps[x] + dist(v, x))
			x = ct[x]
		print(ans)
