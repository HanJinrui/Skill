for _ in range(int(input())):
	A = input()
	print('1' + A if A[0] != '1' else '10' + A[1:])
