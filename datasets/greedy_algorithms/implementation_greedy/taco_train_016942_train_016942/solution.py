for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	g = 1
	while g < n and l[g - 1] == l[g]:
		g += 1
	s = g + 1
	while g + s < n and l[s + g - 1] == l[s + g]:
		s += 1
	x = n // 2
	while x > 0 and l[x - 1] == l[x]:
		x -= 1
	ans = x - g - s
	if ans > g:
		print(g, s, ans)
	else:
		print(0, 0, 0)
