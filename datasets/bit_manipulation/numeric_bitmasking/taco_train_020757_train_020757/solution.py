for _ in range(int(input())):
	(n, a) = map(int, input().split())
	if a % 2:
		if n % 2:
			print('Odd')
		else:
			print('Even')
	elif n == 1:
		print('Even')
	else:
		print('Impossible')
