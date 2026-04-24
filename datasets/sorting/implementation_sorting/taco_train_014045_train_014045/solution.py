x = int(input())
l = list(map(int, input().split()))
d = {}
for i in range(x):
	m = l[i]
	if m in d:
		d[m] = (i, -1 if d[m][1] and i - d[m][0] != d[m][1] else i - d[m][0])
	else:
		d[m] = (i, 0)
b = [(p, d[p][1]) for p in sorted(d.keys()) if d[p][1] >= 0]
print(len(b))
for i in b:
	print(i[0], i[1])
