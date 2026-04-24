(n, c) = map(int, input().split())
c -= n
t = [tuple(map(int, input().split())) for i in range(n)]
x = sum((a / b for (a, b) in t))
if x:
	x = int(c / x)
	while sum((x * a // b for (a, b) in t)) < c:
		x += 1
	print(int(x > 0) + min(((b - x * a % b - 1) // a for (a, b) in t if a > 0)) if sum((x * a // b for (a, b) in t)) == c else 0)
else:
	print(0 if c else -1)
