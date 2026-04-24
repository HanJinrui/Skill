(a, k) = map(int, input().split())
a = list(str(a))
b = ''
while a:
	idx = a.index(max(a[:k + 1]))
	k -= idx
	b += a[idx]
	a.pop(idx)
print(b)
