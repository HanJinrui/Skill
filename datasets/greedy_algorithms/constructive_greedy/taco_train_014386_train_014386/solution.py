(n, a, b) = map(int, input().split())
s = t = 0
for x in map(len, input().split('*')):
	s += x // 2
	t += x % 2
m = min(a, s) + min(b, s)
print(m + min(a + b - m, t))
