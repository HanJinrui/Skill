(N, C) = map(int, input().split())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
A = A * 2
B = B * 2
R = [0 for x in range(2 * N + 1)]
for i in range(2 * N - 1, -1, -1):
	R[i] = R[i + 1] + B[i]
	if R[i] > C:
		print(0)
		exit()
	else:
		R[i] = max(0, R[i] - A[i])
print(sum([1 for i in range(N) if R[i] == 0]))
