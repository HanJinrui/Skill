(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
	if i == 0 or a[i] != a[i - 1]:
		b.append(i)
	else:
		b.append(b[i - 1])
ans = []
for i in range(m):
	(l, r, x) = map(int, input().split())
	ans.append(r if a[r - 1] != x else b[r - 1] if b[r - 1] >= l else -1)
print('\n'.join(map(str, ans)))
