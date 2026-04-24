import sys
t = int(input())
for _ in range(t):
	(n, k) = input().strip().split(' ')
	(n, k) = [int(n), int(k)]
	i = 0
	while 2 ** i <= k:
		i += 1
	ka = 2 ** i - 1
	if k == 1:
		for _ in range(n):
			print(k, end=' ')
		print()
		continue
	elif k == 2 and n % 2 != 0:
		for _ in range(n):
			print(k, end=' ')
		print()
		continue
	if n % 2 == 0:
		i = i - 1
		a1 = 2 ** i
		a2 = a1 - 1
		print(a2, end=' ')
		print(a1, end=' ')
		for _ in range(n - 2):
			print(k, end=' ')
	elif n == 1:
		print(k, end='')
	else:
		i = i - 1
		a1 = 2 ** i
		if k == a1:
			print(k, 1, k - 2, end=' ')
			for _ in range(n - 3):
				print(k, end=' ')
		else:
			print(a1 + 1, 1, a1 - 1, end=' ')
			for _ in range(n - 3):
				print(k, end=' ')
	print()
