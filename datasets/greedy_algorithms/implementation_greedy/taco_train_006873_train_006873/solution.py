for _ in range(int(input())):
	n = int(input())
	x = int(input())
	if '1' not in set(str(x)):
		a = b = x // 2
	else:
		s = str(x)
		k = s.find('1')
		s = s[:k] + '2' + '0' * (n - k - 1)
		a = int(s) // 2
		b = x - a
	print(a)
	print(b)
