t = int(input())
for i in range(t):
	[b, w] = list(map(int, input().split()))
	if b == 0 and w == 1:
		print('W')
		continue
	elif b == 1 and w == 0:
		print('B')
		continue
	elif b == 0 or w == 0:
		print(-1)
		continue
	if b > w:
		print('BW' + 'B' * (b - 1) + 'W' * (w - 1))
	if w >= b:
		print('WB' + 'W' * (w - 1) + 'B' * (b - 1))
	for j in range(b + w):
		if j == 1:
			continue
		print(2, j + 1)
