for s in [*open(0)][2::2]:
	l = [*map(int, s.split())]
	f = 1
	for i in range(30):
		b = 1 << i
		ind = []
		for j in range(len(l)):
			if l[j] & b:
				ind += [j]
		if len(ind) > 1:
			print('YES')
			print(len(ind))
			ind = sorted(ind)
			p = 0
			for x in ind[:-1]:
				print(p + 1, x + 1)
				p = x + 1
			print(p + 1, len(l))
			f = 0
			break
	if f == 1:
		print('NO')
