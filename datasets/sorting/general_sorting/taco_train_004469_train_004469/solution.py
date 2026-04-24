for _ in range(int(input())):
	n = int(input())
	s = input()
	if n <= 2:
		print(s)
	else:
		print(''.join(sorted(s)))
