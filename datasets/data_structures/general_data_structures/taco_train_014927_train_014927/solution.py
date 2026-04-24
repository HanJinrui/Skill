(n, m) = map(int, input().split())
A = list(map(int, input().split()))
for i in range(m):
	(l, r) = map(lambda x: int(x) - 1, input().split())
	if (A[l] < A[l + 1]) == (A[r - 1] > A[r]):
		print('YES')
	else:
		print('NO')
