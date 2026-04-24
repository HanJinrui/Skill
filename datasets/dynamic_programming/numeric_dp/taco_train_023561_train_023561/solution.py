mod = 10 ** 9 + 7
for _ in range(int(input())):
	(n, m, s) = [int(i) for i in input().split()]
	A = [int(i) for i in input().split()]
	dp1 = [0] * (n + 1)
	dp2 = [0] * (n + 1)
	zeros = [0] * (n + 1)
	dp1[s] = 1
	for j in range(m):
		for i in range(1, n + 1):
			if dp1[i] == 0:
				continue
			if i - A[j] > 0:
				dp2[i - A[j]] += dp1[i]
			if i + A[j] <= n:
				dp2[i + A[j]] += dp1[i]
		dp1 = list(dp2)
		dp2 = list(zeros)
	for i in range(1, n + 1):
		print(dp1[i] % mod, end=' ')
	print()
