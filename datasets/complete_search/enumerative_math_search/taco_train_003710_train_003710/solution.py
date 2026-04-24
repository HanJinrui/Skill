for _ in range(int(input())):
	(a, b, c) = map(int, input().split())
	s = input()
	print(s.count('0') * b + s.count('1') * c)
