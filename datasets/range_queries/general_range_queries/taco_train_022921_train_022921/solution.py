T = int(input())
for _ in range(T):
	(N, K) = map(int, input().split())
	(*A,) = map(int, input().split())
	(*D,) = map(int, input().split())
	(*B,) = map(int, input().split())
	P = sorted(zip(A, D))
	A = [a for (a, d) in P]
	D = [d for (a, d) in P]
	left = 0
	right = sum(D) - 1
	for i in range(K):
		if i % 2 == 0:
			left = right - B[i] + 1
		else:
			right = left + B[i] - 1
	cur = 0
	ans = 0
	for i in range(N):
		if left <= cur + D[i] - 1 and cur <= right:
			ans += A[i] * (min(cur + D[i] - 1, right) - max(cur, left) + 1)
		cur += D[i]
	print(ans)
