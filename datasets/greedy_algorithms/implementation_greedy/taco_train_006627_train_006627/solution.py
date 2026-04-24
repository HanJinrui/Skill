n = int(input())
a = b = 0
for i in input().split():
	if i == '25':
		a += 2
	elif i == '50':
		b += 1
	elif b:
		b -= 1
	else:
		a -= 2
	a -= 1
	if a < 0 or b < 0:
		print('NO')
		exit(0)
print('YES')
