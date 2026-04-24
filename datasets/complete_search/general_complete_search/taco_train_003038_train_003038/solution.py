for _ in range(int(input())):
	a = input()
	for i in range(len(a) - 1):
		if int(a[i]) % 2 == int(a[-1]) % 2:
			print('YES')
			break
	else:
		print('NO')
