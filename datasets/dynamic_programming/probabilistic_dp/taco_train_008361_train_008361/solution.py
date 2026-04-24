def Choose(i, s, x, y, cnt):
	if s < 0:
		return 0
	if s == 0:
		return F[cnt] * 2 * F[N - cnt - 2] * (N - cnt - 1)
	if i == N:
		return 0
	if i == x or i == y:
		return Choose(i + 1, s, x, y, cnt)
	if (i, s, x, y, cnt) in Mem:
		return Mem[i, s, x, y, cnt]
	ans = Choose(i + 1, s - A[i], x, y, cnt + 1) + Choose(i + 1, s, x, y, cnt)
	Mem[i, s, x, y, cnt] = ans
	return ans
T = int(input())
F = [1, 1]
for i in range(2, 21):
	F.append(F[-1] * i)
for t in range(T):
	Mem = {}
	ans = 0
	(N, k) = map(int, input().split())
	A = []
	C = []
	ans = 0
	for i in range(N):
		(a, c) = map(int, input().split())
		A.append(a)
		C.append(c)
		if a > k:
			ans += a - k
	P = []
	for i in range(N):
		for j in range(i + 1, N):
			if C[i] == C[j]:
				P.append((i, j))
	for p in P:
		x = p[0]
		y = p[1]
		Lx = A[x]
		Ly = A[y]
		for j in range(0, k):
			e = Choose(0, j, x, y, 0)
			f = Lx + Ly + j - k
			if j + Ly > k:
				f -= j + Ly - k
			if j + Lx > k:
				f -= j + Lx - k
			if f > 0:
				ans += f * (e / F[N])
	print(ans)
