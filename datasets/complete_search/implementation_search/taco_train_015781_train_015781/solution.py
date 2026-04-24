for _ in range(int(input())):
	n = int(input())
	s = 0
	while n >= 1:
		r = int(n ** 0.5)
		s += 1
		n -= r ** 2
	print(s)
