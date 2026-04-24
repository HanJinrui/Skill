(a, b) = map(int, input().split())
n = 0
l = []
m = []
while (n + 1) * (n + 2) // 2 <= a + b:
	n = n + 1
for i in range(n, 0, -1):
	if a >= i:
		a -= i
		l.append(i)
	else:
		m.append(i)
print(len(l))
print(*l)
print(len(m))
print(*m)
