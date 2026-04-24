(n, l) = (int(input()), list(map(int, input().split())))
d = {l[i]: i for i in range(n)}
m = d[l[0]]
a = 1
for i in range(1, n):
	if i > m:
		a = a * 2 % 998244353
	m = max(m, d[l[i]])
print(a)
