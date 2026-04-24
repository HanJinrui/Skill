n = int(input())
a = list(map(int, input().split()))
print('1 1\n' + str((n - 1) * a[0]))
if n >= 2:
	print(2, n)
	print(*[(n - 1) * a[i] for i in range(1, n)])
else:
	print('1 1\n0')
print(1, n)
print(*[-n * a[i] for i in range(n)])
