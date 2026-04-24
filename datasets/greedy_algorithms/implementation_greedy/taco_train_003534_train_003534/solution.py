r = lambda : map(int, input().split())
(a, b) = r()
t = 0
z = 0
for i in a * [0]:
	(c, d) = r()
	t += (c - z - 1) % b + (d - c + 1)
	z = d
print(t)
