T = int(input())
for t in range(0, T):
	(X, Y, N, R) = map(int, input().split())
	p = min((R - N * X) // (Y - X), N)
	if p < 0:
		print(-1)
	else:
		print(N - p, p)
