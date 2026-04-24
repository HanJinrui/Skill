import collections

def solve(u):
	if u not in vis:
		vis.add(u)
		compo.append(u)
		for v in g[u]:
			solve(v)
t = int(input())
for _ in range(t):
	max_t = {}
	(n, m) = map(int, input().split())
	elems = list(map(int, input().split()))
	day_wise = {}
	for i in range(m):
		(d, a, b) = list(map(int, input().split()))
		if d in day_wise:
			day_wise[d].append([a, b])
		else:
			day_wise[d] = [[a, b]]
	for day in sorted(day_wise.keys(), reverse=1):
		vis = set()
		g = {}
		for (u, v) in day_wise[day]:
			if u in g:
				g[u].append(v)
			else:
				g[u] = [v]
			if v in g:
				g[v].append(u)
			else:
				g[v] = [u]
		for u in g:
			compo = []
			solve(u)
			mx = -float('inf')
			for i in compo:
				mx = max(mx, max_t.get(i, i))
			for i in compo:
				max_t[i] = mx
	ans = 0
	for e in elems:
		ans += max_t.get(e, e)
	print(ans)
