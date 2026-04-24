input()
s = list(map(int, input().split()))
d = {}
for a in s:
	d[a] = d.get(a - 1, 0) + 1
a = max(d, key=d.get)
print(d[a])
p = 0
for b in range(a - d[a], a):
	p = s.index(b + 1, p)
	print(p + 1, end=' ')
