q = int(input())
for i in range(q):
	n = int(input())
	ls = list(map(int, input().split()))
	c = [0] * 2001
	for j in ls:
		c[j + 1000] += 1
	ans = 0
	for j in range(2001):
		ans += c[j] * (c[j] - 1) // 2
		for k in range(j + 2, 2001, 2):
			if c[(j + k) // 2]:
				ans += c[j] * c[k]
	print(ans)
