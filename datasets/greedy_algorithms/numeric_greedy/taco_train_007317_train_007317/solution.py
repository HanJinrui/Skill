def f(n):
	return (n - 1) ** 2 // 4
(N, M) = map(int, input().split())
if M > f(N):
	print(-1)
else:
	a = 1
	while f(a) < M:
		a += 1
	X = [i for i in range(1, a + 1)]
	X[-1] += (f(a) - M) * 2
	b = X[-1]
	l = N - len(X)
	X = X + [999999999 - i * (b + 1) for i in range(l)][::-1]
	print(*X)
