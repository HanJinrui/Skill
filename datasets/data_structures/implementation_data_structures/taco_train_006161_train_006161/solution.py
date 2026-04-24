(n, m) = map(int, input().split())
d = {}
for i in range(n):
	(ch, co) = input().split()
	d[ch] = co
dch = dict.fromkeys(sorted([i for i in d]), 0)
dco = dict.fromkeys(sorted([d[i] for i in d]), 0)
for i in range(m):
	ans = input()
	dch[ans] += 1
	dco[d[ans]] += 1
print(max(dco, key=dco.get))
print(max(dch, key=dch.get))
