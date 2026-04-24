mod = 10 ** 9 + 7
for i in range(int(input())):
	n = int(input())
	if n == 1:
		print(2)
		print(0, 1)
	else:
		n = 1 << n
		ans = 4
		for i in range(1, int(n / 2) + 1):
			ans = ans * i % mod
		print(ans)
		print(0, end=' ')
		for i in range(1, int(n / 2)):
			if i & 1:
				print(i, n >> 1 ^ i, end=' ')
			else:
				print(n >> 1 ^ i, i, end=' ')
		print(n >> 1)
