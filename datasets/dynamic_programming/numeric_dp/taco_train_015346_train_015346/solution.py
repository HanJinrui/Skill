def prime(n):
	if n % 2 == 0 and n != 2:
		return False
	for i in range(3, int(n ** 0.5 + 1), 2):
		if n % i == 0:
			return False
	return True
for _ in range(int(input())):
	(x, d) = map(int, input().split())
	ans = 0
	while x % d == 0:
		ans += 1
		x //= d
	if ans == 1:
		print('NO')
	elif ans == 2:
		if prime(x):
			print('NO')
		else:
			print('YES')
	elif prime(x) and prime(d):
		print('NO')
	elif prime(x) and ans == 3 and (d == x ** 2):
		print('NO')
	else:
		print('YES')
