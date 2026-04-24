p = int(input())
print((p // 2) ** 2 + p // 2 * (p % 2))
for i in range(p // 2):
	for j in range(p // 2, p):
		print(i + 1, j + 1)
