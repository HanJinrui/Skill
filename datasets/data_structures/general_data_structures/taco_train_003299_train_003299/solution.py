def pairWiseConsecutive(l):
	for i in range(1, len(l), 2):
		if l[i] != l[i - 1] + 1:
			return False
	return True
