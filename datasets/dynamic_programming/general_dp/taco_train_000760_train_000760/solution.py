def solve():
	(n, m) = map(int, input().split())
	if m < n:
		n = m
	a = []
	i = 0
	s = 0
	while s <= n:
		i += 1
		s += i
	r = 0
	s -= i
	j = i - 1
	for i in range(n - s):
		r += (j + 1) * (j + 1)
		j -= 1
	while j > 0:
		r += j * j
		j -= 1
	print(r)
t = 1
t = int(input())
for _test_ in range(t):
	solve()
