for _ in range(int(input())):
	n = int(input())
	a = [0]
	a.extend(list(map(int, input().split())))
	a.append(10000000000)
	start = end = -1
	x = y = -1
	i = 1
	while i <= n:
		while i <= n and a[i-1] < a[i] and a[i+1] > a[i]:
			i += 1
		if i == n+1:
			break
		else:
			x = i
			i += 1
			while i <= n and a[i-1] > a[i] and a[i+1] < a[i]:
				i += 1
			if i == n+1:
				break
			else:
				y = i
				if a[y] > a[x-1]:
					if a[y+1:] == sorted(a[y+1:]):
						start, end = x, y
					else:
						break
				i += 1
	print(start, end)
