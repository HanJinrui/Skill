def isBinary(str):
	return all((int(i) in [0, 1] for i in str))
