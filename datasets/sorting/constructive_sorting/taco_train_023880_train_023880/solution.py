(n, m) = map(int, input().split())
a = {}
for i in range(m):
	a[i + 1] = []
for i in range(n):
	s = input().split()
	a[int(s[1])] += [(int(s[2]), s[0])]
for i in range(m):
	z = sorted(a[i + 1])[::-1]
	print('?' if len(z) > 2 and z[1][0] == z[2][0] else z[0][1] + ' ' + z[1][1])
