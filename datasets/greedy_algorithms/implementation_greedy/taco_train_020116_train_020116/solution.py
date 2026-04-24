n = int(input()) // 3
s = input()
(c1, c2, c3, c4, c6) = [s.count(_) for _ in '12346']
if c1 != n or c2 < c4 or c1 != c2 + c3 or (c1 != c4 + c6):
	print(-1)
	exit()
print('1 2 4\n' * c4 + '1 3 6\n' * c3 + '1 2 6\n' * (n - c4 - c3))
