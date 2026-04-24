import sys
input = sys.stdin.readline
for _ in range(int(input())):
	(n, m) = map(int, input().split())
	if n > m or (n % 2 == 0 and m % 2 == 1):
		print('NO')
	else:
		print('YES')
		l = []
		if n % 2 == 1:
			print('1 ' * (n - 1) + str(m - n + 1))
		else:
			print('1 ' * (n - 2) + (str((m - (n - 2)) // 2) + ' ') * 2)
