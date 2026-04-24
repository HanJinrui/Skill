T = int(input())
for _ in range(T):
	(n, k, m) = map(int, input().split())
	b = [int(i) for i in input().split()]
	ff = False
	for (p, i) in enumerate(b):
		if i - p - 1 >= k >> 1 and n - i - len(b) + p + 1 >= k >> 1:
			ff = True
	if b == [int(i) + 1 for i in range(n)]:
		print('YES')
	elif k > 1 and (n - m) % (k - 1) == 0:
		if ff:
			print('YES')
		else:
			print('NO')
	else:
		print('NO')
