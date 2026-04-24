import math
for _ in range(int(input())):
	n = int(input()) - 1
	l = 2
	while math.gcd(l, n - l) != 1:
		l += 1
	print(l, n - l, 1)
