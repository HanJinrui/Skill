I = lambda : [*map(int, input().split())]
(n, a) = I()
x = 0
for c in I():
	x = x * a + c
(m, b) = I()
y = 0
for c in I():
	y = y * b + c
print('<=>'[(x >= y) + (x > y)])
