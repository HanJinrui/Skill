for _ in range(int(input())):
	x = int(input())
	l = list(map(float, input().split()))
	a = sum(l) / x
	if a in l:
		print(l.index(a) + 1)
	else:
		print('Impossible')
