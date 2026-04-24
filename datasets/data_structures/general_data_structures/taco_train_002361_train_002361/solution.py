for i in range(int(input())):
	(N, M) = map(int, input().split())
	A = [int(k) for k in input().split()]
	if M - len(set(A)) > 0:
		print('Yes')
	else:
		print('No')
