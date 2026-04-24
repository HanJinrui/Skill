for _ in range(int(input())):
	(N, X) = map(int, input().split())
	A = list(map(int, input().split()))
	print('YES' if X <= max(A) else 'NO')
