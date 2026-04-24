a = input()
b = [input() for i in range(int(input()))]
e = 0
for i in b:
	x = y = 0
	for j in a:
		if j == i[0]:
			x += 1
		elif j == i[1]:
			y += 1
		else:
			e += min(x, y)
			x = y = 0
	e += min(x, y)
print(e)
