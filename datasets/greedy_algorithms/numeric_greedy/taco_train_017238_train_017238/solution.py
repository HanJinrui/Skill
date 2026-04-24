(a, b, f, k) = map(int, input().split())
(s, t) = (0, b - f)
g = f = a - f
for i in range(k):
	if t < 0:
		break
	if k - 1 - i:
		g += f
	if t < g:
		(s, t) = (s + 1, b)
	t -= g
	g = f = a - f
print(-1 if t < 0 else s)
