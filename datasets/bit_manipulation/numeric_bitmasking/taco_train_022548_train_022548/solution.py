n = int(input())
l = list(map(int, input().split()))
x = 0
for i in range(30):
	y = 0
	for j in l:
		if j & 2 ** i:
			y += 1
	x += y * (y - 1) // 2 * 2 ** i
print(x)
