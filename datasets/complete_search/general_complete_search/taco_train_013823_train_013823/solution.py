for _ in range(int(input())):
	n = int(input())
	if n % 7 == 0:
		print(n)
	else:
		r = n % 7
		if n % 10 + 7 - r < 10:
			print(n + 7 - r)
		else:
			print(n - r)
