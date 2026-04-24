h = r = 0
for _ in [0] * int(input()):
	x = int(input())
	r += abs(x - h) + 2
	h = x
print(r - 1)
