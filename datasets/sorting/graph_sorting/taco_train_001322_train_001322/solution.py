(n, m, k) = input('').split(' ')
n = int(n)
m = int(m)
k = int(k)
ts = []
ps = []
for p in range(k + 1):
	_ = input('')
	pic = ''
	for line in range(n):
		pic += input('')
	ps.append(pic)
	w = 0
	for i in range(1, n - 1):
		for j in range(1, m - 1):
			z = i * m + j
			if pic[z] not in (pic[z + 1], pic[z - 1], pic[z + m], pic[z - m]):
				w += 1
	ts.append((n * m - w, p))
ts = sorted(ts)
print(ts[0][1] + 1)
ops = []
for r in range(k):
	pic1 = ps[ts[r][1]]
	pic2 = ps[ts[r + 1][1]]
	for i in range(1, n - 1):
		for j in range(1, m - 1):
			z = i * m + j
			if pic1[z] != pic2[z]:
				ops.append('1 %i %i' % (i + 1, j + 1))
	ops.append('2 ' + str(ts[r + 1][1] + 1))
print(len(ops))
for op in ops:
	print(op)
