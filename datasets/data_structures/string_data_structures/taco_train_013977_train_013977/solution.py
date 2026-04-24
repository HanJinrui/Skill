def findMissing(A, B, N, M):
	B = set(B)
	return [j for j in A if j not in B]
