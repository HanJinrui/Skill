for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	if len(set(a)) < n or n & 1 == 0:
		print('YES')
	else:
		print('NO')
