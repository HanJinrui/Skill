def booleanMatrix(matrix):
	r = len(matrix)
	c = len(matrix[0])
	rows = [any(row) for row in matrix]
	colums = [any(col) for col in zip(*matrix)]
	for i in range(r):
		for j in range(c):
			matrix[i][j] = int(any((rows[i], colums[j])))
