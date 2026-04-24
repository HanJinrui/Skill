import math
for _ in [0] * int(input()):
	a = int(input())
	d = math.gcd(a, 180)
	print(-180 // d * (-2 * d // (180 - a)))
