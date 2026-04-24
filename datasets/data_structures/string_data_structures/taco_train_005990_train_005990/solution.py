for _ in range(int(input())):
	(n, x, y) = map(int, input().split())
	s = input()
	if '1' in s and '0' in s:
		print(min(x, y))
	else:
		print(0)
