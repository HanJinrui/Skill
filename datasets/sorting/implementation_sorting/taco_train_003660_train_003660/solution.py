(n, m) = map(int, input().split())
(x, y) = map(int, input().split())
s = 0
for i in range(int(input())):
	(dx, dy) = map(int, input().split())
	(a, b) = (n, m)
	if dy > 0:
		a = (m - y) // dy
	elif dy < 0:
		a = (y - 1) // -dy
	if dx > 0:
		b = (n - x) // dx
	elif dx < 0:
		b = (x - 1) // -dx
	d = min(a, b)
	x += d * dx
	y += d * dy
	s += d
print(s)
