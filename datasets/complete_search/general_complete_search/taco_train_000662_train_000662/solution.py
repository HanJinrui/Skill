for i in range(int(input())):
	(R1, W1, C1) = map(int, input().split())
	(R2, W2, C2) = map(int, input().split())
	if (R1 > R2) + (W1 > W2) + (C1 > C2) >= 2:
		print('A')
	else:
		print('B')
