from math import ceil, log2
(A, B, C, D) = sorted(map(int, input().split()))
X = Y = 0
L = [0] * 2 ** ceil(log2(D + 1))
for i in range(1, C + 1):
	for j in range(i, D + 1):
		L[i ^ j] += 1
		X += 1
for i in range(1, B + 1):
	for j in range(1, min(A, i) + 1):
		Y += X - L[i ^ j]
	for l in range(i, D + 1):
		L[i ^ l] -= 1
		X -= 1
print(Y)
