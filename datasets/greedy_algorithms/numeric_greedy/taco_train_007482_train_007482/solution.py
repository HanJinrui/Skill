for _ in range(int(input())):
	n = int(input())
	A = list(map(int, input().split()))
	X = sum(A)
	if X % n:
		print(-1)
		continue
	X //= n
	print(3 * n - 3)
	for i in range(1, n):
		print(1, i + 1, -A[i] % (i + 1))
		print(i + 1, 1, (A[i] - 1) // (i + 1) + 1)
	for i in range(1, n):
		print(1, i + 1, X)
