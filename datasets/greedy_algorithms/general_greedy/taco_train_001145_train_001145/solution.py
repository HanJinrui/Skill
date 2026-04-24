for s in [*open(0)][2::2]:
	print(sum((int(x) + (x > '0') for x in s[:-2])) + int(s[-2]))
