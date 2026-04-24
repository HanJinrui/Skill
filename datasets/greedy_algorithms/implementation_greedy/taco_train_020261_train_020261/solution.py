I = lambda : map(int, input().split())
(n, m) = I()
C = [0] * n
for (L, R, t, c) in sorted(([*I()] for _ in range(m)), key=lambda x: x[2]):
	for i in range(L - 1, R):
		if not C[i]:
			C[i] = c
print(sum(C))
