(m, n) = map(int, input().split())
A = [[1] * n] * m
B = [[0] * n] * m
C = []
for i in range(m):
	L = list(map(int, input().split()))
	C.append(L)
	for j in range(len(L)):
		if L[j] == 0:
			A[i] = [0] * n
			for k in range(m):
				A[k][j] = 0
for p in range(m):
	for w in range(n):
		if A[p][w] == 1:
			B[p] = [1] * n
			for s in range(m):
				B[s][w] = 1
if B == C:
	print('YES')
	for i in A:
		print(*i)
else:
	print('NO')
