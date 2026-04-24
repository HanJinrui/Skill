for z in range(int(input())):
	(n, k) = [int(x) for x in input().split()]
	a = list(input())
	d = 0
	for i in range(1, n):
		if a[i] == a[i - 1]:
			d += 2
		else:
			d += 1
	for x in input().split():
		k = int(x) - 1
		if k > 0:
			if a[k - 1] == a[k]:
				d -= 1
			else:
				d += 1
		if k < n - 1:
			if a[k + 1] == a[k]:
				d -= 1
			else:
				d += 1
		if a[k] == '0':
			a[k] = '1'
		else:
			a[k] = '0'
		print(d)
