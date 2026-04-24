for _ in range(int(input())):
	n = int(input())
	s = input()
	a = s.count('1')
	b = n - a
	if a == 0 or b == 0:
		print('Bob')
	elif a == 1 or b == 1:
		print('Alice')
	elif n & 1:
		print('Alice')
	else:
		print('Bob')
