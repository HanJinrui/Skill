import math
(a, b, c, d) = [int(i) for i in input().split()]
g = math.gcd(c, d)
c //= g
d //= g
e = min(a // c, b // d)
print(e * c, e * d)
