(N, K) = map(int, input().split(' '))
(A, B, C, D, M) = ([None] * (K + 1), [3] * (K + 1), [0] * (N + 1), [0] * (N + 1), 10 ** 9 + 7)
(B[0], B[1], A[0], C[1]) = (1, 2, 1, 1)
for n in range(4, N + 1):
	for k in range(1, K + 1):
		A[k] = (B[k] + A[k - 1] - (0 if k < n else B[k - n])) % M
	(B, A) = (A, B)
for i in range(2, N + 1):
	for j in range(1, i + 1):
		D[j] = (C[j - 1] + (i - 1) * C[j]) % M
	(C, D) = (D, C)
print('%d %d' % (B[-1], sum(C[N - min(K, N - 1):N + 1]) % M))
