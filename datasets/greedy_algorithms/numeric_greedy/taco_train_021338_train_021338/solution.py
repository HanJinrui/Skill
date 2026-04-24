for _ in range(int(input())):
	(n, k, b, s) = map(int, input().split())
	nums = 0
	if k * b <= s <= k * b + n * (k - 1):
		while s - k >= b * k:
			s -= k - 1
			nums += 1
		print('0 ' * (n - nums - 1) + f'{k - 1} ' * nums + str(s))
	else:
		print(-1)
