big = 10 ** 9 + 7

def multMatrix(A, B):
	res = [[0] * k for _ in range(k)]
	mult = lambda x, y: x * y
	for (j, col) in enumerate(zip(*B)):
		for (i, row) in enumerate(A):
			res[i][j] = sum(map(mult, row, col)) % big
	return res

def squareMatrix(A):
	res = [[0] * k for _ in range(k)]
	mult = lambda x, y: x * y
	for (j, col) in enumerate(zip(*A)):
		for (i, row) in enumerate(A):
			res[i][j] = sum(map(mult, row, col)) % big
	return res

def powMatrix(A, p):
	if p == 1:
		return A
	X = powMatrix(A, p // 2)
	if p & 1:
		return multMatrix(A, squareMatrix(X))
	else:
		return squareMatrix(X)
(k, n) = [int(x) for x in input().split(' ')]
F = [int(x) for x in input().split(' ')]
C = [int(x) for x in input().split(' ')]
ck = C[-1]
M = [[0] * k for _ in range(k)]
for i in range(k - 1):
	M[i][i + 1] = ck
M[-1] = [1] + [-x for x in C[:-1]]
if n - k + 1 == 0:
	print(' '.join((str(x) for x in F)))
	exit()
M = powMatrix(M, n - k + 1)
ck_inv = pow(ck, big - 2, big)
F0 = [sum(map(lambda x, y: x * y, row, F)) * pow(ck_inv, n - k + 1, big) % big for row in M]
print(' '.join((str(x) for x in F0)))
