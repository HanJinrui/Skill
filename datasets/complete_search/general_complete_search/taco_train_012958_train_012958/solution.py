L = lambda : list(map(int, input().split()))
(n, m, c) = L()
(A, B) = (L(), L())
for i in range(n - m + 1):
	for j in range(i, i + m):
		A[j] += B[j - i]
		A[j] %= c
print(*A)
