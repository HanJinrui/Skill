t = int(input())
for _ in range(t):
	input()
	m = {}
	for s in input().split():
		m.setdefault(s[1:], set()).add(s[0])
	ans = 0
	for s in m.values():
		for s1 in m.values():
			it = len(s1.intersection(s))
			ans += (len(s1) - it) * (len(s) - it)
	print(ans)
