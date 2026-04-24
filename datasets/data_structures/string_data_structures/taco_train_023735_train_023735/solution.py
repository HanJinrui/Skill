def countRev(s):
	k = 0
	k1 = 0
	if len(s) % 2:
		return -1
	for i in s:
		if i is '{':
			k = k + 1
		elif k:
			k = k - 1
		else:
			k1 = k1 + 1
			k = k + 1
	return k1 + k // 2
