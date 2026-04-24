for i in range(int(input())):
	n = int(input())
	x = input()
	if x[-1] in x[:-1]:
		print('YES')
	else:
		print('NO')
