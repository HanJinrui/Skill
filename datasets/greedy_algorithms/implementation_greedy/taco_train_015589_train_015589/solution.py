(n, m) = map(int, input().split())
a = set(list(map(int, input().split())))
k = 1
b = []
while k <= m:
	if k not in a:
		b.append(k)
		m -= k
	k += 1
print(len(b))
print(*b)
