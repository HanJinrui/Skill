import math
x = int(input())
i = int(x ** 0.5)
while i + 1 and (math.gcd(x // i, i) > 1 or x % i):
	i -= 1
print(i, x // i)
