for i in range(int(input())):
	s = input()
	s = list([s[i:i + 2] for i in range(len(s) - 1)])
	print(len(set(s)))
