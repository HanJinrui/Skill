for i in range(int(input())):
	s = input()
	print('YES' if len(s) % 2 == 0 and len(s) // 2 == s.count(max(s, key=s.count)) else 'NO')
