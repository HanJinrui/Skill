for _ in range(int(input())):
	N = int(input())
	A = [0] + list(map(int, input().split())) + [1440]
	ANS = 0
	for i in range(N + 1):
		ANS += (A[i + 1] - A[i]) // 120
	if ANS >= 2:
		print('YES')
	else:
		print('NO')
