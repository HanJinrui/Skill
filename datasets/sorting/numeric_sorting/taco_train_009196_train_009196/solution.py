for s in [*open(0)][2::2]:
	(*a, l) = s.split()
	print(*(['NO'], ['YES\n', l] + a)[l != a[0]])
