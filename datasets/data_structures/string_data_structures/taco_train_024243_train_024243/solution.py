for _ in range(int(input())):
	a = input()
	b = input()
	n = [i for i in b if i in a]
	print(len(n))
