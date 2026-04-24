T = int(input())
for _ in range(T):
	(N, P) = map(int, input().split()[:2])
	if P > 2:
		print(('a' + 'b' * (P - 2) + 'a') * (N // P))
	else:
		print('impossible')
