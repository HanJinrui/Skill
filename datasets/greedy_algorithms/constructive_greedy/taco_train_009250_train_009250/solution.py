for s in [*open(0)][1:]:
	n = int(s.split()[0])
	print(('abc' * n)[:n])
