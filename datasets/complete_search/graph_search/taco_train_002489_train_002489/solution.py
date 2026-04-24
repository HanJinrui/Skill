f = lambda : map(int, input().split())
(n, m) = f()
(p, s) = ([], [set() for i in range(n + 1)])
for j in range(m):
	(a, b) = f()
	p += [(a, b, c) for c in s[a].intersection(s[b])]
	s[a].add(b)
	s[b].add(a)
k = [len(s[i]) for i in range(n + 1)]
print(min((k[a] + k[b] + k[c] for (a, b, c) in p)) - 6 if p else -1)
