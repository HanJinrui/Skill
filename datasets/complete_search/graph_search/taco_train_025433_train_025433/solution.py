(x, y, z) = map(int, input().split())
c = 0
while x + z != y:
	c += 1
	x -= 1
	z -= 1
	if x < 0 or z < 0:
		print('Impossible')
		exit()
print(x, z, c)
