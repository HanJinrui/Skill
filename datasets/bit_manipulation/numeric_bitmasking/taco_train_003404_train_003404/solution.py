t = int(input())
for i in range(t):
	(n, k) = map(int, input().split())
	a = [*map(int, input().split())]
	num = prv = 0
	for x in a:
		num += x - prv - 1
		num //= 2
		prv = x
	num += n - prv
	print(n - k - bin(num).count('1'))
