n = int(input())
a = int(input())
b = int(input())
y = 0
while n % a != 0 and n >= 0:
	n -= b
	y += 1
if n < 0:
	print('NO')
else:
	print('YES')
	print(n // a, y)
