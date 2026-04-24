A = [list(map(int, input().split())) for _ in range(3)]
s = sum(map(sum, A)) // 2
for i in range(3):
	A[i][i] = s - sum(A[i])
	print(*A[i])
