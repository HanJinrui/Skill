for _ in range(int(input())):
	a = int(input())
	b = input()
	if b[:a // 2] == b[a // 2:]:
		print('YES')
	else:
		print('NO')
