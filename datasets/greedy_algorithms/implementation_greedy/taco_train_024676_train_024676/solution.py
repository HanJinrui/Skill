I = input
for _ in [0] * int(I()):
	i = 0
	n = int(I())
	a = (*map(int, I().split()), -2)
	while a[i] >= i:
		i += 1
	while a[i - 1] >= n - i:
		i += 1
	print('YNeos'[i < n::2])
