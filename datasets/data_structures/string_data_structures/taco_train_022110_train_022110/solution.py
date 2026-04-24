n = int(input())
for i in range(n):
	k = int(input())
	k1 = input()
	s = set(k1)
	x = 0
	for i in s:
		if k1.count(i) % 2 == 1:
			x += 1
	if x >= 1:
		print('NO')
	else:
		print('YES')
