from math import factorial as f
from functools import reduce as d
from operator import mul as m
from itertools import product as p
(u, t, r, s) = (map, sum, range, input())
print(t((f(t(x)) // d(m, u(f, x)) - f(t(x) - 1) * x[0] // d(m, u(f, x)) * (x[0] > 0) for x in p(*[r(y and 1, y + 1) for y in [s.count(str(d)) for d in r(10)]]))))
