I = input
I()
r = p = 0
for (x, y) in zip(I(), I()):
	r += x > y
	p += x < y
print(r and p // r + 1 or -1)
