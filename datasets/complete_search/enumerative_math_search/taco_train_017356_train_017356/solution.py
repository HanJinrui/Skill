import math
(n, m, k) = map(int, input().split())
print(k // (n * m // math.gcd(n, m)))
