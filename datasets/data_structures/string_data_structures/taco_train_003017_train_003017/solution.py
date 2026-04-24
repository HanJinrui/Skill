def uniqueRow(row, col, matrix):
	ls = []
	for i in range(row):
		x = matrix[i * col:i * col + col]
		if x not in ls:
			ls.append(x)
	return ls
