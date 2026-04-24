from math import ceil
R = lambda : map(int, input().split())
for j in range(int(input())):
	(hc, dc) = R()
	(hm, dm) = R()
	(k, w, a) = R()
	for i in range(k + 1):
		if ceil(hm / (dc + (k - i) * w)) <= ceil((hc + i * a) / dm):
			print('YES')
			break
	else:
		print('NO')
