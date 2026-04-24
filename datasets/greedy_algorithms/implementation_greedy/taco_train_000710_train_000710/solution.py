for s in [*open(0)][2::2]:
	a = list(map(int, s.split()))[1:-1]
	if len(a) == 1 and a[0] & 1 or a.count(1) == len(a):
		print(-1)
	else:
		print(sum([(i + 1) // 2 for i in a]))
