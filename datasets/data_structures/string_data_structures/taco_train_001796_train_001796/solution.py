for _ in range(int(input())):
	x = int(input())
	s = input()
	p = set(s)
	if len(p) == len(s):
		print(-1)
	else:
		print(len(s) - 2)
