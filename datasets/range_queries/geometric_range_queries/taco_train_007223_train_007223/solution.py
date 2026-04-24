from collections import defaultdict
for _ in range(int(input())):
	(n, m) = map(int, input().split())
	(l1, l2) = ([], [])
	for _ in range(n):
		(a, b) = map(int, input().split())
		l1.append((a, 1))
		l1.append((b, 2))
	for _ in range(m):
		(a, b) = map(int, input().split())
		l1.append((a, 3))
		l1.append((b, 4))
	l1.sort()
	ans = 0
	(a, b, prev) = (0, 0, 0)
	for (i, e) in enumerate(l1):
		ans += a * b * (e[0] - prev)
		if e[1] == 1:
			a += 1
		elif e[1] == 2:
			a -= 1
		elif e[1] == 3:
			b += 1
		else:
			b -= 1
		prev = e[0]
	print(ans)
