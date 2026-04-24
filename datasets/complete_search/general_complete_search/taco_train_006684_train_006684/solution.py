import sys
n = int(input().strip())
for i in range(1, n):
	mvs = []
	for j in range(1, n):
		v = set([])
		q = [(0, 0)]
		ql = [0]
		while q:
			x = q.pop(0)
			lv = ql.pop(0)
			if x == (n - 1, n - 1):
				mvs.append(lv)
				break
			if x in v:
				continue
			v.add(x)
			l = [y for y in [(x[0] + j, x[1] + i), (x[0] + i, x[1] + j), (x[0] + j, x[1] - i), (x[0] + i, x[1] - j), (x[0] - j, x[1] - i), (x[0] - i, x[1] - j), (x[0] - j, x[1] + i), (x[0] - i, x[1] + j)] if y[0] >= 0 and y[0] < n and (y[1] >= 0) and (y[1] < n)]
			q.extend(l)
			ql.extend([lv + 1 for _ in l])
		if not q:
			mvs.append(-1)
	print(' '.join([str(x) for x in mvs]))
