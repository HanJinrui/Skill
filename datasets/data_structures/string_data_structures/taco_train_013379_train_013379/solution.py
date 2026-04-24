for i in range(int(input())):
	n = int(input())
	s = input()
	t = s.count('01')
	v = s.count('10')
	print(t + v + 1)
