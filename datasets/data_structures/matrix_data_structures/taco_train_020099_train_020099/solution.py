def rotate(matrix):
	l = []
	for i in zip(*matrix):
		l = [i] + l
	matrix[:] = l[:]
