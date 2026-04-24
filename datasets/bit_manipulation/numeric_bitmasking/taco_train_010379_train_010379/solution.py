for _ in range(int(input())):
	n = int(input())
	if n % 4 == 0:
		print(n + 3)
	elif n % 4 == 1:
		print(n)
	else:
		print(3)
