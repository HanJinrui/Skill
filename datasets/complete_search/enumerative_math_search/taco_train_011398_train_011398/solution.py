R = lambda : map(int, input().split())
(n, k, m) = R()
inp = R()
r = s = i = 0
for x in reversed(sorted(inp)):
	i += 1
	s += x
	if n - i <= m:
		r = max(r, (s + min(k * i, m - n + i)) / i)
print(r)
