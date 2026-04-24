for i in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	x = [a[0]]
	c = 1
	for i in a[1:]:
		if i < min(x[-1:-6:-1]):
			c += 1
		x.append(i)
	print(c)
