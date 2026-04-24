(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
c = 0
p = a[-1]
q = a[0]
v = 1
m = 0
while q != p:
	while q == a[v]:
		v = v + 1
	if c + v > k:
		m = m + 1
		c = v
	else:
		c = c + v
	q = q - 1
if c > 0:
	m = m + 1
print(m)
