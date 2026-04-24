for _ in range(int(input())):
	n = int(input())
	if n % 2:
		print('YES')
		k = 2 * n
		for i in range(1, n + 1, 2):
			print(i, k)
			k -= 1
		for i in range(2, n + 1, 2):
			print(i, k)
			k -= 1
	else:
		print('NO')
