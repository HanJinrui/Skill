for i in range(int(input())):
	n = int(input())
	s = 0
	for i in range(n):
		s = s ^ int(input(), 2)
	print(str(bin(s)).count('1'))
