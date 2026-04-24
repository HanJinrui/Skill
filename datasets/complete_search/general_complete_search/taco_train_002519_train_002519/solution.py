n = int(input())
a = 1234567
b = 123456
c = 1234
while n >= 0:
	m = n
	while m >= 0:
		if m % c == 0:
			print('YES')
			exit()
		m -= b
	n -= a
print('NO')
