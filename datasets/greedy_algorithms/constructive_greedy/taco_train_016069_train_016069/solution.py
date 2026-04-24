n = int(input())
for i in range(n):
	for j in range(n):
		if j % 2 == 0:
			print(j * n + i + 1, end=' ')
		else:
			print((j + 1) * n - i, end=' ')
	print()
