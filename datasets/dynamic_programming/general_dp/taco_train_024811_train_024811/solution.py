A = [0, 0, 0, 0, 0, 2, 3, 15, 2, 0]
B = [0, 0, 0, 0, 0, 4, 9, 13, 17, 2]
C = [1, 9, 90, 303, 280, 218, 95, 101, 295]
M = 10 ** 9 + 7
q = int(input())
for Q in range(q):
	n = int(input())
	for i in range(len(A), n):
		A.append(2 * (A[i - 5] + B[i - 5]) % M)
		B.append((A[i - 1] + A[i - 5] + 2 * B[i - 5]) % M)
	print(C[n] if n < len(C) else (5 * A[n - 1] + 9 * A[n - 2] + 19 * A[n - 3] + 6 * A[n - 4] + 3 * A[n - 5] + 2 * B[n - 1] + 5 * B[n - 2] + 20 * B[n - 3] + 5 * B[n - 4] + 4 * B[n - 5]) % M)
