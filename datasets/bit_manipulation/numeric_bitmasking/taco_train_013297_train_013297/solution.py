for _ in range(int(input())):
	n = int(input())
	ans = -1
	curr = 1
	while True:
		if curr == n:
			ans = -1
			break
		elif curr > n:
			break
		ans += curr * ((n + curr) // (2 * curr))
		curr *= 2
	print(ans)
