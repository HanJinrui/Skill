def sol(L, A, N, D):
	if A < D or N < D or L < N:
		print('SAD')
	elif D == 1:
		print(L * A)
	else:
		m = 0
		cm = (N - 1) // (D - 1)
		for c in range(cm, 0, -1):
			a1 = N + (c - 1) - c * (D - 1)
			n = (L - a1) // c
			h = (L - a1) % c
			if n > A - 1 or (n == A - 1 and h > 0):
				break
			s = A * a1 + (A - 1 + A - n) * n // 2 * c + h * (A - n - 1)
			if s <= m:
				break
			m = s
		print('SAD' if m == 0 else m)
for a0 in range(int(input())):
	sol(*[int(x) for x in input().split(' ')])
