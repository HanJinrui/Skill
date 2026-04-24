from math import gcd
from functools import reduce
for _ in range(int(input())):
	(n, a) = (int(input()), list(map(int, input().split())))
	print(n if reduce(gcd, a) == 1 else -1)
