from math import sqrt
t = int(input())
for i in range(t):
	(a, b) = map(int, input().split())
	if int(sqrt(a)) > int((-1 + sqrt(1 - 4 * -b)) / 2):
		print('Limak')
	else:
		print('Bob')
