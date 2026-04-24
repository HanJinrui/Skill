t = [98] * 51
for s in [*open(0)][2::2]:
	for x in [0] + s.split():
		t[int(x)] ^= 1
		print(''.join(map(chr, t)))
