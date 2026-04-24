for _ in range(int(input())):
	(a, b) = map(int, input().split())
	print('01' * min(a, b) + ((a - b) * '0' if a > b else (b - a) * '1'))
