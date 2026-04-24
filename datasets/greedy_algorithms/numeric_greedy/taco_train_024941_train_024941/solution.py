n = int(input())
b = 2
a = 1
d = 0
while b <= n:
	(a, b) = (b, a + b)
	d += 1
print(d)
