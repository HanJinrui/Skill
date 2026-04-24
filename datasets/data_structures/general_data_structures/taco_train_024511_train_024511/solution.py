from collections import Counter
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	total = sum(a)
	prefix = 0
	d = Counter()
	for i in range(n):
		remains = total - a[i]
		if not remains % 2:
			ans += d[remains // 2]
		prefix += a[i]
		d[prefix] += 1
	d.clear()
	suffix = 0
	for i in range(n - 1, -1, -1):
		remains = total - a[i]
		if not remains % 2:
			ans += d[remains // 2]
		suffix += a[i]
		d[suffix] += 1
	print(ans)
