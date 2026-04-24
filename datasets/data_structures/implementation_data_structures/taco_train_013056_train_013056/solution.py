(n, s) = (int(input()), set())
for a in map(int, input().split()):
	s.add(a)
	while n in s:
		print(n, end=' ')
		n -= 1
	print()
