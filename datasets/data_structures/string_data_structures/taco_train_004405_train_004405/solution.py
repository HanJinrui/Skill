import sys
import bisect
input = sys.stdin.readline
T = int(input())
for _ in range(T):
	s = input()
	(x1, y1) = map(int, input().split())
	q = int(input())
	(l, r, u, d) = (s.count('L'), s.count('R'), s.count('U'), s.count('D'))
	(xmp, ymp) = (x1 + r, y1 + u)
	(xmn, ymn) = (x1 - l, y1 - d)
	for _ in range(q):
		(x, y) = map(int, input().split())
		if x >= xmn and y >= ymn and (x <= xmp) and (y <= ymp):
			print('YES {}'.format(abs(x - x1) + abs(y - y1)))
		else:
			print('NO')
