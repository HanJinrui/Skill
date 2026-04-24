for _ in range(int(input())):
	(N, C) = map(int, input().split())
	A = list(map(int, input().split()))
	print('Yes' if sum(A) <= C else 'No')
