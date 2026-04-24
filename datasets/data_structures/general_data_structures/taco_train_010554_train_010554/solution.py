def saveIronman(s):
	a = ''.join([i for i in s.lower() if i.isalnum()])
	return a == a[::-1]
