for _ in range(int(input())):
	s = {*input()} | {*input()}
	print(len(s) - 1)
