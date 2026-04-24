tt = int(input())
while tt:
	(h, c, t) = map(int, input().split())
	if h == t:
		print(1)
	elif t <= (h + c) / 2:
		print(2)
	else:
		k = (t - c - 1) // (2 * t - h - c)
		ans = 2 * k + 1
		if (4 * k * k - 1) * (2 * t - h - c) >= 2 * (h - c) * k:
			ans -= 2
		print(ans)
	tt -= 1
