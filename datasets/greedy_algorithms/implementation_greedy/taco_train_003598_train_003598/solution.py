t = int(input())
for k in range(t):
	n = int(input())
	a = 0
	for i in range(n):
		(x, l, f) = list(map(int, input().split()))
		while a > x:
			x += f
		a = x + l
	print(a)
