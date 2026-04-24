(n, m, k) = map(int, input().split())
a = [input().split() for _ in ' ' * n]
r = {str(i): i - 1 for i in range(1, n + 1)}
c = {str(i): i - 1 for i in range(1, m + 1)}
ans = []
for _ in range(k):
	(ch, x, y) = input().split()
	if ch == 'c':
		(c[x], c[y]) = (c[y], c[x])
	elif ch == 'r':
		(r[x], r[y]) = (r[y], r[x])
	else:
		ans.append(a[r[x]][c[y]])
print('\n'.join(ans))
