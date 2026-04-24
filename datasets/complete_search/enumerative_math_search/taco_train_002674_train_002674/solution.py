for i in range(int(input())):
	n = int(input())
	s = input()
	a = s.count('0')
	if 120 - a >= 90:
		print('YES')
	else:
		print('NO')
