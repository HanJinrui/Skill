def f(x, t):
	y = x
	while sum((y * a // b for (a, b) in t)) < c:
		y += 1000000
	while y - x > 1:
		z = (x + y) // 2
		d = sum((z * a // b for (a, b) in t))
		if d < c:
			x = z
		else:
			y = z
	return y
(n, c) = map(int, input().split())
c -= n
t = [tuple(map(int, input().split())) for i in range(n)]
x = sum((a / b for (a, b) in t))
if x:
	x = f(int(c / x), t)
	print(int(x > 0) + min(((b - x * a % b - 1) // a for (a, b) in t if a > 0)) if sum((x * a // b for (a, b) in t)) == c else 0)
else:
	print(0 if c else -1)
