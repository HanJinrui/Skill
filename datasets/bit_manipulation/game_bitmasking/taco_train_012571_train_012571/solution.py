from functools import reduce
for i in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	print(['Second', 'First'][reduce(lambda x, y: x ^ y, l) == 0 or n % 2 == 0])
