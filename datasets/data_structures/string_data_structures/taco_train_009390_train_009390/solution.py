for _ in range(int(input())):
	N = int(input())
	S = input()
	c = S.count('1')
	print(c * (c + 1) // 2)
