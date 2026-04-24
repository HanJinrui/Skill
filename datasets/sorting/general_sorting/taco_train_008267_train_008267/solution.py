(x1, y1) = map(int, input().split())
(x2, y2) = map(int, input().split())
n = int(input())
s = input()
(x, y, dx, dy) = (0, 0, [0], [0])
for c in s:
	if c == 'U':
		y += 1
	elif c == 'D':
		y -= 1
	elif c == 'L':
		x -= 1
	else:
		x += 1
	dx.append(x)
	dy.append(y)
(ans, L, R) = (-1, 0, 10 ** 15)
while L <= R:
	M = (L + R) // 2
	x = M // n * dx[n] + dx[M % n]
	y = M // n * dy[n] + dy[M % n]
	if abs(x - (x2 - x1)) + abs(y - (y2 - y1)) <= M:
		ans = M
		R = M - 1
	else:
		L = M + 1
print(ans)
