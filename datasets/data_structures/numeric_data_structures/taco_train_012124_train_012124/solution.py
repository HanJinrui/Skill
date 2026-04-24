from itertools import *
R = lambda : map(int, input())
M = 998244353
input()
(s, p) = (0, 1)
for (x, y) in zip([*R()][::-1], [*accumulate(R())][::-1]):
	s = (s + p * x * y) % M
	p = p * 2 % M
print(s)
