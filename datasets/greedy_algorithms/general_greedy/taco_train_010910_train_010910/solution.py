(n, m) = map(int, input().split())
a = list(map(int, input().split()))
kek = set()
p = {a[-1]}
for i in range(m):
	kek.add(tuple(map(int, input().split())))
a = a[::-1]
for c in a[1:]:
	f = True
	for x in p:
		if (c, x) not in kek:
			p.add(c)
			break
print(n - len(p))
