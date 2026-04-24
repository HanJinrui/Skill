for _ in range(int(input())):
	s = input()
	res = s.count('xy')
	s = s.replace('xy', '')
	res += s.count('yx')
	print(res)
