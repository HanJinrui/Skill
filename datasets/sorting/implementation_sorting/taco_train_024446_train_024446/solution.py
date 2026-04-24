for s in [*open(0)][1:]:
	print(sorted(s.split(), key=int)[1])
