def subsetPairNotDivisibleByK(arr, N, K):
	f = [0 for i in range(K)]
	for i in range(N):
		f[arr[i] % K] += 1
	if K % 2 == 0:
		f[K // 2] = min(f[K // 2], 1)
	res = min(f[0], 1)
	for i in range(1, K // 2 + 1):
		res += max(f[i], f[K - i])
	return res
