f = lambda q: 1 + int((1 + 8 * q) ** 0.5) >> 1
(a, b, c, d) = map(int, input().split())
(x, y) = (f(a), f(d))
if x * x - x - 2 * a or y * y - y - 2 * d:
	t = 'Impossible'
elif a + b + c == 0:
	t = '1' * y
elif b + c + d == 0:
	t = '0' * x
elif b + c - x * y:
	t = 'Impossible'
elif c:
	t = '1' * (y - b // x - 1) + '0' * (b % x) + '1' + '0' * (x - b % x) + '1' * (b // x)
else:
	t = '0' * x + '1' * y
print(t)
