for s in [*open(0)][2::2]:
	print(len(''.join((' *'[x > '0'] for x in s.split())).split(None, 1)))
