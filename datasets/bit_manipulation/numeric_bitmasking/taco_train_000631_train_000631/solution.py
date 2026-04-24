n = int(input())
a = [int(x) for x in input().split()]
xor = 0
if len(a) % 2 == 0:
	for i in a:
		xor ^= i
if n % 2 == 0 and xor != 0:
	print('NO')
else:
	print('YES')
	arr = [(i, i + 1, i + 2) for i in range(1, n - 1, 2)]
	arr += arr[::-1][1:]
	print(len(arr))
	for (i, j, k) in arr:
		print(i, j, k)
