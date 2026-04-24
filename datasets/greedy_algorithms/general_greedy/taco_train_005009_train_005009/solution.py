from itertools import *
R = lambda : map(int, input().split())
(n, m) = R()
a = [0, *R()] + [m] * (n % 2 + 1)
d = [x - y for (x, y) in zip(a[1:], a)]
print(sum(d[::2]) + max(1, *accumulate((d[i - 1] - d[i] for i in range(n + n % 2, 0, -2)))) - 1)
