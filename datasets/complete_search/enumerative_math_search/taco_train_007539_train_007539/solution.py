(x, y) = (int(input()), 0)
(h, m) = map(int, input().split())
while not '7' in f'{h}{m}':
	y += 1
	(h, m) = divmod((h * 60 + m - x) % 1440, 60)
print(y)
