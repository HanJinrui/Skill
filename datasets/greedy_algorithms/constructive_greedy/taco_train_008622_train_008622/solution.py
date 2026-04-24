n = int(input())
T = []
for i in range(n):
	T.append(input()[::-1])
Val = ['0', '1']
S = 0
L1 = [0] * n
C1 = [0] * n
for diag in range(n - 1):
	for i in range(diag + 1):
		(l, c) = (L1[i], C1[diag - i])
		if T[i][diag - i] != Val[(l + c) % 2]:
			S += 1
			L1[i] = 1 - l
			C1[diag - i] = 1 - c
L2 = [0] * n
C2 = [0] * n
for diag in range(n - 1):
	for i in range(diag + 1):
		(l, c) = (L2[i], C2[diag - i])
		if T[n - diag + i - 1][n - i - 1] != Val[(l + c) % 2]:
			S += 1
			L2[i] = 1 - l
			C2[diag - i] = 1 - c
for i in range(n):
	if Val[(L1[i] + L2[i] + C1[n - i - 1] + C2[n - i - 1]) % 2] != T[i][n - i - 1]:
		S += 1
print(S)
