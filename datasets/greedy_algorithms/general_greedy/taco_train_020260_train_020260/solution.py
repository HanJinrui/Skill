for _ in range(int(input())):
	n = int(input())
	s = input()
	c = 0
	for i in set(s):
		c += s.count(i + i)
	print(n - c)
