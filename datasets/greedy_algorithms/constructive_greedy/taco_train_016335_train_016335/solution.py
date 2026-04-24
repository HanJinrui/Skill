(n, k, p) = map(int, input().split())
for i in range(p):
	pos = int(input())
	if n % 2:
		if pos == n:
			print('X' if k > 0 else '.', end='')
		elif k * 2 > n + 1:
			print('X' if pos & 1 == 0 or (n - pos) // 2 + n // 2 + 1 <= k else '.', end='')
		else:
			print('X' if pos & 1 == 0 and (n + 1 - pos) // 2 < k else '.', end='')
	elif k * 2 > n:
		print('X' if pos & 1 == 0 or (n - pos + 1) // 2 + n // 2 <= k else '.', end='')
	else:
		print('X' if pos & 1 == 0 and (n - pos + 2) // 2 <= k else '.', end='')
