(h, w) = map(int, input().split())
a = []
for _ in range(h):
	a.append(input())
(i, j, k) = (0, 0, 0)
while i < h:
	if a[i][j] == '*':
		k += 1
	if i != h - 1 and a[i + 1][j] == '*' or j == w - 1:
		i += 1
	else:
		j += 1
print(k)
