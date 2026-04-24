m = int(input())
a = 0
while m > 0:
	a += 5
	b = a
	while b % 5 == 0:
		b //= 5
		m -= 1
if m < 0:
	print(0)
else:
	print(5)
	print(a, a + 1, a + 2, a + 3, a + 4)
