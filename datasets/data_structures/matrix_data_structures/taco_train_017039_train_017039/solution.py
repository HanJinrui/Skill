def isToepliz(A, n, m):
	for i in range(n - 1):
		for j in range(m - 1):
			if A[i][j] != A[i + 1][j + 1]:
				return False
	return True
