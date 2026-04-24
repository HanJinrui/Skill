n = int(input())
k = 0
while n % 7 != 0:
	n -= 4
	k += 1
if n < 0:
	print('-1')
else:
	print(k * '4' + n // 7 * '7')
