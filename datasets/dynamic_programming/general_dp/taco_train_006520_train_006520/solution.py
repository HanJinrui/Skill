for _ in range(int(input())):
	(n, rs, p1, p2) = (int(input()), 0, (0, 0), (0, 0))
	for t in sorted(map(lambda li: (int(li[1]), int(li[0])), [input().split(' ') for _ in range(n)])):
		if t[1] > p2[0]:
			(rs, p2) = (rs + 1, t)
		elif t[1] > p1[0]:
			(p1, p2, rs) = (p2, t, rs + 1)
	print(rs)
