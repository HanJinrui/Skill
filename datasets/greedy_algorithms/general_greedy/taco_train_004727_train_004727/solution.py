(n, k) = map(int, input().split())
b = 0
a = []
for i in range(n):
	(l, t) = map(int, input().split())
	if t:
		a.append(l)
	else:
		b += l
a.sort(key=lambda x: -x)
print(b + sum(a[:k]) - sum(a[k:]))
