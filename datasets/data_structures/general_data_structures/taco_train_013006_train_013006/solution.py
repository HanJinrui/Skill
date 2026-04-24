for _ in range(int(input())):
	(n, k) = map(int, input().split())
	A = [int(x) for x in input().split()]
	M = A[::2]
	T = A[1::2]
	for _ in range(k):
		minval = min(T)
		T[T.index(min(T))] = max(M)
		M[M.index(max(M))] = minval
	if sum(T) > sum(M):
		print('YES')
	else:
		print('NO')
