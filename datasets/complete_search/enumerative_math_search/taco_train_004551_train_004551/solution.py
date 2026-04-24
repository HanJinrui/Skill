(r1, r2) = map(int, input().split())
(c1, c2) = map(int, input().split())
(d1, d2) = map(int, input().split())
x = (d1 + c1 - r2) // 2
y = r1 - x
z = c1 - x
w = d1 - x
if 1 <= x <= 9 and 1 <= y <= 9 and (1 <= z <= 9) and (1 <= w <= 9) and (len(set([x, y, z, w])) == 4):
	print(x, y)
	print(z, w)
else:
	print(-1)
