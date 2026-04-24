for _ in range(int(input())):
	inps = input()
	print('yes' if len(inps) > len(set(inps)) else 'no')
