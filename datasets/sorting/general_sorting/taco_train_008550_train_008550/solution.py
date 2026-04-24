for _ in range(int(input())):
	n = int(input())
	a = [int(s) for s in input().split(' ')]
	zc = 0
	for i in range(n - 1):
		a.sort(reverse=True)
		while a[-1] == 0:
			zc += 1
			a.pop()
		for i in range(len(a) - 1):
			a[i] -= a[i + 1]
		if zc:
			zc -= 1
		else:
			a.pop()
	if zc:
		print(0)
	else:
		print(a[0])
