I = input
for c in '0' * int(I()):
	I()
	s = I()
	print(len(2 * max(s, s[::-1]).lstrip(c) or s))
