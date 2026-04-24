import sys
(n, m, s) = map(int, sys.stdin.readline().split())
p = [[] for i in range(n + 1)]
for i in range(m):
	(u, v, w) = map(int, input().split())
	p[u].append((v, w))
	p[v].append((u, w))
l = int(input())
t = [l + 1] * (n + 1)
(t[s], q) = (0, {s})
while q:
	u = q.pop()
	r = t[u]
	for (v, w) in p[u]:
		if r + w < t[v]:
			q.add(v)
			t[v] = r + w
(s, r) = (0, 2 * l)
for u in range(1, n + 1):
	d = t[u]
	if d < l:
		for (v, w) in p[u]:
			if d + w > l and (t[v] + d + w > r or (u < v and t[v] + d + w == r)):
				s += 1
	elif d == l:
		s += 1
print(s)
