for i in range(int(input())):
	n = int(input())
	s = input()
	a = s.count('1')
	b = s.count('0')
	string = '01' * (n // 2)
	if s == string:
		print(n // 2)
	elif a < b:
		print(a)
	elif b < a:
		print(b)
	else:
		print(a - 1)
