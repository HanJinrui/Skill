for _ in range(int(input())):
	s = input()
	print(1 if s == s[::-1] else 2)
