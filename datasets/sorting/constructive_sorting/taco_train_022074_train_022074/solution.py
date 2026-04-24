input()
a = sorted(map(int, input().split()))
b = a[::2]
c = a[1::2]
if len(set(b)) + len(set(c)) < len(a):
	print('NO')
else:
	print('YES', len(b), *b, len(c), *c[::-1])
