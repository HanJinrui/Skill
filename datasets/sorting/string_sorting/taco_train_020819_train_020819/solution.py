n = int(input())
a = input()
for i in range(1, n):
	if a[i] < a[i - 1]:
		print('YES')
		exit(print(i, i + 1))
print('NO')
