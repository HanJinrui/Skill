for s in [*open(0)][2::2]:
	print(s.strip('0 \n').count('0'))
