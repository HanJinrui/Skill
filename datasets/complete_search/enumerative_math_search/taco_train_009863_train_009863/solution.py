import math
for _ in range(int(input())):
	(m, b) = map(int, input().split())
	print(math.gcd(m, b) * 2)
