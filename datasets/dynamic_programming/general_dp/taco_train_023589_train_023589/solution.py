(n, la, lb) = map(int, input().split(' '))
(F, M) = ([0] * (n + 2), 10 ** 9 + 7)
for a in map(int, input().split(' ')):
	if F[a - 1] == 1 or F[a + 1] == 1:
		M = None
	F[a] = 1
for b in map(int, input().split(' ')):
	if F[b] == 1 or F[b - 1] == -1 or F[b + 1] == -1:
		M = None
	F[b] = -1
if M == None:
	print(0)
else:
	(A, B, FF) = ([0] * (n + 1), [0] * (n + 1), [None] * (n + 1))
	for i in range(1, n + 1):
		FF[i] = F[i] - F[i - 1]
	A[1] = 1
	for i in range(2, n + 1):
		for j in range(1, i + 1):
			if FF[i] > 0:
				B[j] = (B[j - 1] + A[j - 1]) % M
			elif FF[i] < 0:
				B[j] = (B[j - 1] + A[i - 1] - A[j - 1]) % M
			else:
				B[j] = (B[j - 1] + A[i - 1]) % M
		(A, B) = (B, A)
	print(A[n])
