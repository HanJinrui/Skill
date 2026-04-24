import math
for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	d = 0
	for i in l:
		d = math.gcd(d, i)
	if d == 1:
		print(0)
	elif math.gcd(d, n) == 1:
		print(1)
	elif math.gcd(d, n - 1) == 1:
		print(2)
	else:
		print(3)
