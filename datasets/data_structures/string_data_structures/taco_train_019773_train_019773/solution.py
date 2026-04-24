for _ in range(int(input())):
	n = int(input())
	s = input()
	new = s.replace('01', 'x1').replace('10', '1x')
	print(new.count('0'))
