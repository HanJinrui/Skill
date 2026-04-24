tn = int(input())
for _ in range(tn):
	n = int(input())
	ar = dict()
	for i in range(1, n + 1):
		ar[i] = list(map(int, input().split()))
	(mvsm, midx) = (-1, -1)
	for i in range(1, n + 1):
		visli = {i}
		tdis = 0
		queue = [(i, 0)]
		while queue:
			(nd, dis) = queue.pop(0)
			tdis += dis
			for x in ar[nd]:
				if x not in visli:
					visli.add(x)
					queue.append((x, dis + 1))
		if mvsm == -1:
			mvsm = tdis
			midx = i
		elif mvsm > tdis:
			mvsm = tdis
			midx = i
	print(midx, '{:.6f}'.format(mvsm / n))
