def fin(c, x):
	return (x + c - 1) // c

def ck(x, b):
	r = (n, n)
	for i in range(b, n):
		r = min(r, (i + fin(c[i][0], x), i))
	return r

def sol(r, l):
	if r[0] <= n and l[0] <= n and (r[1] < n) and (l[1] < n):
		print('Yes')
		print(r[0] - r[1], l[0] - l[1])
		print(' '.join([str(x[1]) for x in c[r[1]:r[0]]]))
		print(' '.join([str(x[1]) for x in c[l[1]:l[0]]]))
		return True
	else:
		return False
(n, x1, x2) = [int(x) for x in input().split()]
c = sorted([(int(x), i + 1) for (i, x) in enumerate(input().split())])
r1 = ck(x1, 0)
l1 = ck(x2, r1[0])
r2 = ck(x2, 0)
l2 = ck(x1, r2[0])
if not sol(r1, l1) and (not sol(l2, r2)):
	print('No')
