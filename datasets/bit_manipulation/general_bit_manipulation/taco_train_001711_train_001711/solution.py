for _ in range(int(input())):
	x = int(input())
	print((1 << x.bit_length()) - 1 - x)
