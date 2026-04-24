(n, m) = map(int, input().split())
l = []
anss = [1] * (n + 1)
for i in range(m):
	l.append(list(map(int, input().split())))
for i in range(m - 1):
	for j in range(i + 1, m):
		sx = l[i][0] - l[j][0]
		sy = l[i][1] - l[j][1]
		ans = 2
		if sx:
			if sy:
				x = (l[i][0] * sy - l[i][1] * sx) / sy
				if 1 <= x <= n and int(x) == x:
					for k in range(j + 1, m):
						if l[k][1] * sx == sy * (l[k][0] - l[i][0]) + l[i][1] * sx:
							ans += 1
					anss[int(x)] = max(ans, anss[int(x)])
		elif 1 <= l[i][0] <= n:
			for k in range(j + 1, m):
				if l[k][0] == l[i][0]:
					ans += 1
			anss[l[i][0]] = max(anss[l[i][0]], ans)
print(sum(anss[1:]))
