for _ in range(eval(input())):
	N, M = list(map(int, input().split()))
	A = list(map(int, input().split()))

	P, P2 = [], []
	for _ in range(M):
		ans = [A[1]]
		for j in range(1, N - 1):
			if A[j - 1] and A[j + 1]:
				ans.append(1)
			else:
				ans.append(0)

		ans.append(A[N - 2])
		A = ans[:]
		if ans == P:
			break
		elif ans == P2:
			y = M - _+1
			if y % 2 == 0:
				break
			else:
				A = P
				break
		P2 = P
		P = A

	print(' '.join([str(i) for i in A]))
