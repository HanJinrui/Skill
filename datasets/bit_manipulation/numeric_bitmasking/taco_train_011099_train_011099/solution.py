for _ in range(int(input())):
	n = int(input())
	s = input()
	if s == '1' or s == '10':
		print('NO')
	else:
		print('YNEOS'[s.count('1') > 3::2])
