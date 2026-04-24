import sys
R = lambda : map(int, next(sys.stdin).split())
(t,) = R()
while t:
	t -= 1
	(n, x) = R()
	(*a,) = R()
	print('YNEOS'[a[-x:x] != sorted(a)[-x:x]::2])
