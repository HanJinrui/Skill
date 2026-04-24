for _ in range(int(input())):
	n = int(input())
	if n == 1:
		print(1, end='')
	elif n % 2 == 0:
		for i in range(1, n * 2, 2):
			print(i, end=' ')
	else:
		for i in range(2, n * 2 + 1, 2):
			print(i, end=' ')
	print()
