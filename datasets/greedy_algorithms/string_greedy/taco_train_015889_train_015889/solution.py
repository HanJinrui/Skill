c = ord('a') - 1
for s in map(ord, input()):
	if s > c + 1:
		print('NO')
		exit()
	c = max(c, s)
print('YES')
