for _ in range(int(input())):
	(n, A, B) = (int(input()), [], [])
	for _ in range(n):
		A.append(input().split())
	for _ in range(n):
		B.append(input().split())
	for i in range(n):
		for j in range(n):
			if A[i][j] != B[i][j] and A[i][j] == B[j][i]:
				for k in range(n):
					(A[k][j], A[j][k]) = (A[j][k], A[k][j])
	if A == B:
		print('Yes')
	else:
		print('No')
