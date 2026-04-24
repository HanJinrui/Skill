for _ in range(int(input())):
	(N, Q) = map(int, input().split())
	x = list(map(int, input().split()))
	assert len(x) == N
	queries = []
	for j in range(Q):
		(a, p, q) = map(int, input().split())
		assert 1 <= p <= q <= N
		queries.append((q - 1, p - 1, a, j))
	assert len(queries) == Q
	queries.sort()
	answers = [0] * Q
	maxi = [-1] * 65536
	qnxt = 0
	for i in range(N):
		xi = x[i]
		assert 0 <= xi < 32768
		k = xi + 32768
		while k > 0:
			if maxi[k] < i:
				maxi[k] = i
			k //= 2
		while qnxt < Q and queries[qnxt][0] == i:
			(q, p, a, j) = queries[qnxt]
			qnxt += 1
			k = 1
			b = 14
			while b >= 0:
				prefer = 1 - (a >> b) & 1
				k = 2 * k + prefer
				if maxi[k] < p:
					k ^= 1
				assert maxi[k] >= p
				b -= 1
			assert k >= 32768
			answers[j] = a ^ k - 32768
	for v in answers:
		print(v)
