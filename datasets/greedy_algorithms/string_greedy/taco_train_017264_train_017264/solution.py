for t in range(int(input())):
	s = ''.join([*(input() for x in '_' * (int(input()) * 2 + 1))])
	for i in s:
		if s.count(i) % 2:
			print(i)
			break
