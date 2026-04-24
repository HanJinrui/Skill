for _ in range(int(input())):
	(a, b) = map(int, input().split())
	sum = 0
	a = a - 1
	for i in range(1, b + 1, 2):
		sum += (b // i - a // i) * i
	print(sum)
