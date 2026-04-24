s = input()
(a, b, c) = (s.count(x) for x in '01?')
if a + c > b:
	print('00')
if a + c + 2 > b >= a - c:
	if s[-1] != '?':
		if s[-1] == '0':
			print('10')
		else:
			print('01')
	else:
		if a + c > b:
			print('01')
		if b + c > a + 1:
			print('10')
if b + c > a + 1:
	print('11')
