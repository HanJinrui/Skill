for _ in range(int(input())):
	(n, m) = map(int, input().split())
	a = list(map(int, input().split()))
	ans = 0
	tab = set()
	for i in range(m):
		if a[i] in tab:
			continue
		if len(tab) < n:
			tab.add(a[i])
			ans += 1
			continue
		x = set()
		for j in range(i + 1, m):
			if a[j] in tab and len(x) < n - 1:
				x.add(a[j])
		tab = x
		tab.add(a[i])
		ans += 1
	print(ans)
