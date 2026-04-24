def ans(x, y):
	x = bin(x)[2:]
	y = bin(y)[2:]
	return int(x + y, 2) - int(y + x, 2)
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	if n <= 800:
		x = max([ans(i, j) for j in a for i in a])
		print(x)
	else:
		y = max(a)
		x = max([abs(ans(i, y)) for i in a])
		print(x)
