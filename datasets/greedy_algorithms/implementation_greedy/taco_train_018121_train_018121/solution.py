x = y = 0
r = 1
for _ in [0] * int(input()):
	(a, b) = map(int, input().split())
	r += max(0, min(a, b) - max(x, y) + (x != y))
	(x, y) = (a, b)
print(r)
