from collections import defaultdict
for _ in range(int(input())):
	n = int(input())
	(c, a) = ([[0 for _ in range(2)] for _ in range(n)], defaultdict(list))
	for i in range(n):
		for j in list(map(int, input().split()))[1:]:
			if j < 0:
				c[i][0] += 1
				a[-j].append([i, 0])
			else:
				c[i][1] += 1
				a[j].append([i, 1])
	ans = 0
	for i in sorted(a.keys()):
		if len(a[i]) > 1:
			ans += 1
			for j in a[i]:
				c[j[0]][j[1]] -= 1
				ans += c[j[0]][j[1]]
		else:
			c[a[i][0][0]][a[i][0][1]] -= 1
			ans += c[a[i][0][0]][a[i][0][1] ^ 1]
	print(ans)
