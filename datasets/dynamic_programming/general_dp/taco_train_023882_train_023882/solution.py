def func():
	MOD = 10 ** 9 + 9
	Max = 10 ** 5 + 1
	nCr = [[1]]
	for n in range(1, 27):
		m = [1]
		for k in range(1, n):
			m.append(nCr[-1][k] + nCr[-1][k - 1])
		m.append(1)
		nCr.append(m)
	DP = [[]]
	for k in range(1, 27):
		FDP = [1]
		for i in range(1, Max):
			temp = FDP[-1] * k
			if i % 2 == 0:
				temp = temp - FDP[i // 2]
			FDP.append(temp % MOD)
		DP.append(FDP)
	for t in range(int(input())):
		(N, K) = map(int, input().split())
		G = [0]
		for i in range(1, K + 1):
			G.append(pow(i, N, MOD) - DP[i][N] - sum((G[j] * nCr[i][j] for j in range(1, i))) % MOD)
		print(G[-1] * nCr[26][K] % MOD)
func()
