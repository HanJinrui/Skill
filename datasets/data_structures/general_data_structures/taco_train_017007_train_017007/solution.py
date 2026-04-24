a = [list(map(int, input().split())) for i in range(6)]
m = -9999999999
for i in range(4):
	for j in range(4):
		s = sum(a[i][j:j + 3]) + a[i + 1][j + 1] + sum(a[i + 2][j:j + 3])
		if s > m:
			m = s
print(m)
