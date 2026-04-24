def downwardDiagonal(N, A):
	out = []
	for j in range(2 * N):
		for i in range(N):
			if j - i >= 0 and j - i < N:
				out.append(A[i][j - i])
	return out
