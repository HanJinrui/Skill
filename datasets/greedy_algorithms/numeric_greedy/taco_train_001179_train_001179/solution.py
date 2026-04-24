for s in [*open(0)][1:]:
	n = int(s)
	print(('9' + '8901234567' * n)[:n])
