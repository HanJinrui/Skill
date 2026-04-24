for _ in range(int(input())):
	n = int(input())
	if n == 2:
		p = 1
	elif n % 4 == 0:
		p = n // 2 + 1
	elif n % 2 == 0:
		p = n // 2 + 2
	else:
		p = n // 2 + 1
	q = n - p
	print(p * q - 1)
