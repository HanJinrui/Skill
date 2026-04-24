T = int(input())
INF = 10 ** 20

def solve(s):
	n = len(s)
	prv = [None for i in range(n + 1)]
	p = 0
	q = -INF
	for i in range(n):
		prv[i] = p < q
		(p, q) = (max(p, q), p + s[i])
	prv[n] = p < q
	v = n
	res = [0] * n
	while v > 0:
		if prv[v]:
			res[v - 1] = 1
			v -= 2
		else:
			v -= 1
	return res
ans = []
for _ in range(T):
	N = int(input())
	(*A,) = map(int, input().split())
	B = [0] * N
	B[0] = A[0] < A[1]
	B[-1] = A[-2] > A[-1]
	for i in range(1, N - 1):
		B[i] = A[i - 1] > A[i] < A[i + 1]
	cur = 0
	res = 0
	while cur < N:
		while cur < N and (not B[cur]):
			cur += 1
		if cur == N:
			break
		s = [A[cur]]
		r = [cur]
		while cur + 2 < N and B[cur + 2] and (A[cur] + A[cur + 2] >= A[cur + 1]):
			cur += 2
			s.append(A[cur])
			r.append(cur)
		cur += 1
		rs = solve(s)
		for (i, f) in zip(r, rs):
			if f:
				A[i] = -A[i]
	ans.append(' '.join(map(str, A)))
print(*ans, sep='\n')
