d = {}
l = []
(n1, n2, n3) = map(int, input().split())
s = n1 + n2 + n3
for i in range(s):
	x = int(input())
	d[x] = d.get(x, 0) + 1
for x in d:
	if d.get(x) >= 2:
		l.append(x)
print(len(l))
for x in sorted(l):
	print(x)
