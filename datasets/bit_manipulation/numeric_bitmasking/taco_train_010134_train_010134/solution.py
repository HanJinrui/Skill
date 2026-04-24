sevseg = [126, 48, 109, 121, 51, 91, 95, 112, 127, 123]
for _ in range(int(input())):
	n = int(input())
	(x, y) = ([None] * n, [None] * n)
	mini = 8
	maxi = -1
	for i in range(n):
		(x[i], y[i]) = map(int, input().rstrip().split())
	badaflag = 0
	for check in range(128):
		flag = 1
		for i in range(n):
			if bin(sevseg[x[i]] & check).count('1') != y[i]:
				flag = 0
				break
		if flag:
			deadCell = 7 - bin(check).count('1')
			mini = min(mini, deadCell)
			maxi = max(maxi, deadCell)
			badaflag = 1
	if badaflag:
		print(mini, maxi)
	else:
		print('invalid')
