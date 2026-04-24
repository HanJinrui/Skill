(n, k) = map(int, input().split())
(*v, l) = input()
sets = [(0, 0)]
d = {'W': +1, 'D': 0, 'L': -1}
for c in v:
	(ms, mx) = sets[-1]
	ns = max(1 - k, ms + d.get(c, -1))
	nx = min(k - 1, mx + d.get(c, +1))
	if ns > nx:
		print('NO')
		exit(0)
	sets.append((ns, nx))
(ms, mx) = sets[-1]
if mx == k - 1 and l in '?W':
	cur = k - 1
	ans = ['W']
elif ms == 1 - k and l in '?L':
	cur = 1 - k
	ans = ['L']
else:
	print('NO')
	exit(0)
ans += list(reversed(v))
for (i, (c, (s, x))) in enumerate(zip(reversed(v), sets[-2::-1])):
	if c == '?':
		ans[i + 1] = next((p for (p, q) in d.items() if s <= cur - q and cur - q <= x))
	cur -= d[ans[i + 1]]
print(''.join(reversed(ans)))
