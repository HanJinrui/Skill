(x, y, a, b) = map(int, input().split())
C = [(i, j) for i in range(max(a, b + 1), x + 1) for j in range(b, min(i, y + 1))]
print(len(C))
for c in C:
	print(*c)
