inp = lambda : map(int, input().split())
(n, m) = inp()
link = [i + 1 for i in range(n + 3)]
ans = [0] * (n + 1)
for _ in range(m):
	(l, r, x) = inp()
	pt = l
	while pt <= r:
		if ans[pt] == 0 and pt != x:
			ans[pt] = x
		nxt = link[pt]
		if pt < x:
			link[pt] = x
		else:
			link[pt] = r + 1
		pt = nxt
print(*ans[1:])
