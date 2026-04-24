for _ in range(int(input())):
	(x, y) = map(int, input().split())
	z = x ^ y
	ans = [2]
	for n in (x, y, z):
		if n % 2:
			ans.append(n ^ 2)
	print(*sorted(ans))
