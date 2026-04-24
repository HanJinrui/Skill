for _ in range(int(input())):
	(n, k) = map(int, input().split())
	A = list(map(int, input().split()))
	ans = 0
	m = max(A)
	for i in range(k - 1, n):
		if A[i] == m:
			ans += n - i
	print(ans)
