x = []
y = []
for i in range(3):
	(a, b) = input().split()
	x.append(int(a))
	y.append(int(b))
print(3)
for i in range(3):
	print(str(sum(x) - 2 * x[i]) + ' ' + str(sum(y) - 2 * y[i]))
