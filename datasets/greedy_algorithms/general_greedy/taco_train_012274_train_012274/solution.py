R = lambda : map(int, input().split())
(n, k) = R()
d = {}
for x in R():
	i = 0
	while x:
		l = d.setdefault(x, [])
		l += (i,)
		x >>= 1
		i += 1
print(min((sum(sorted(d[x])[:k]) for x in d if len(d[x]) >= k)))
