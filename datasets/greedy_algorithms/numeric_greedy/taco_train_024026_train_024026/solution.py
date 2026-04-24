(n, q) = (int(input()), 0)
import math
for i in map(int, input().split()):
	q = math.gcd(q, i)
print(q * n)
