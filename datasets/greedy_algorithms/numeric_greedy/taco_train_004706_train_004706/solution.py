(r, c) = map(int, input().split())
if max(r, c) == 1:
	print(0)
else:
	for i in range(1, r + 1):
		for j in range(1, c + 1):
			print(i * (j + r) if r <= c else j * (i + c), end=' ')
		print()
