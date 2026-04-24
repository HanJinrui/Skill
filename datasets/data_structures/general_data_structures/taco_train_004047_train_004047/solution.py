import sys
f = sys.stdin
next(f)
for (n, a, b) in zip(f, f, f):
	r = sum(((ord(y) - ord(x)) % 26 for (x, y) in zip(a, b))) % 26
	print(r if r < 14 else 26 - r)
