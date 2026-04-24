f = lambda : map(int, input().split())
(n, m) = f()
p = []
for i in range(m):
	(a, b) = f()
	p.append((a, 1 - b, i))
p.sort()
k = j = 0
s = [0] * m
(u, v) = (1, 3)
for (a, b, i) in p:
	if not b:
		k += j
		s[i] = (j + 1, j + 2)
		j += 1
	elif k:
		k -= 1
		s[i] = (u, v)
		if v - u - 2:
			u += 1
		else:
			(u, v) = (1, v + 1)
	else:
		print(-1)
		exit(0)
for (x, y) in s:
	print(x, y)
