n = [min(int(i), 9 - int(i)) for i in input()]
if n[0] < 1:
	n[0] = 9
print(*n, sep='')
