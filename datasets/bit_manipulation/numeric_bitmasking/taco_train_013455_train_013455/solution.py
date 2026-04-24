t = int(input())
while t > 0:
	a = input()
	b = input()
	if len(set(list(a))) != 1:
		dist = []
		for (i, j) in zip(a, b):
			if i != j:
				dist.append(i)
		print('Lucky Chef')
		d = dist.count('1')
		e = dist.count('0')
		print(max(d, e))
	else:
		print('Unlucky Chef')
	t -= 1
