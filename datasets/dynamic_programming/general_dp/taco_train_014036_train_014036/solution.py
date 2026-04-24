(m, n) = map(int, input().strip().split(' '))
land = []
for j in range(0, m):
	land.append(input())
fence = 0
for j in range(0, m - 1):
	for i in range(0, n - 1):
		if land[j][i] == '.' and land[j][i + 1] == '.' and (land[j + 1][i] == '.'):
			w = 1
			while i + w < n and land[j][i + w] == '.':
				h = 1
				while j + h < m and land[j + h][i] == '.' and (land[j + h][i + w] == '.'):
					check = 1
					for x in range(0, w):
						if land[j + h][i + x] != '.':
							check = 0
							break
					if check:
						l = 2 * w + 2 * h
						if l > fence:
							fence = l
					h = h + 1
				w = w + 1
if fence == 0:
	print('impossible')
else:
	print(fence)
