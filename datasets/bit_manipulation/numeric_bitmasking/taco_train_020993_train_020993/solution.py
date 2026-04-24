import functools
import operator

def LII():
	return [int(x) for x in input().split()]

def II():
	return int(input())
for _ in range(int(input())):
	n = II()
	a = LII()
	b = LII()
	sets = [a[0] | b[0]] + [x & ~y | z for (x, y, z) in zip(a[1:], a[:-1], b[1:])]
	resets = [~x & y | ~z for (x, y, z) in zip(b[:-1], b[1:], a[:-1])] + [~a[-1] | ~b[-1]]
	xor_sets = functools.reduce(operator.xor, sets, 0)
	arbs = functools.reduce(operator.or_, (~x & ~y for (x, y) in zip(sets, resets)), 0)
	print(arbs | xor_sets)
