for s in [*open(0)][2::2]:
	print(ord(sorted(list(s))[-1]) - 96)
