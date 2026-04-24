(n, k) = map(int, input().split())
l = [1, 2, 3, 5]
print((6 * n - 1) * k)
for i in range(n):
	for j in l:
		print((6 * i + j) * k, end=' ')
	print()
