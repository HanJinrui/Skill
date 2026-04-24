T = int(input())
for _ in range(T):
	(N, K) = map(int, input().split())
	A = list(map(int, input().split()))

	def length(getMask, ignoreMask):
		assert getMask & ignoreMask == 0
		C = [0]
		D = {0: 0}
		res = float('inf')
		for (i, elt) in enumerate(A):
			presum = C[-1] ^ elt & ~ignoreMask
			C.append(presum)
			comp = presum ^ getMask
			if comp in D:
				l = i + 1 - D[comp]
				res = min(res, l)
			D[C[-1]] = i + 1
		return res
	res = length(K, 0)
	ignoreMask = -1 & (1 << 32) - 1
	getMask = 0
	for k in range(31, -1, -1):
		ignoreMask ^= 1 << k
		if K & 1 << k != 0:
			getMask |= 1 << k
		else:
			getMask |= 1 << k
			res = min(res, length(getMask, ignoreMask))
			getMask ^= 1 << k
	if res == float('inf'):
		print(-1)
	else:
		print(res)
