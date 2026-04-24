def solve(c, n, bs):
	errstr = '0' * (c + 1) + '1'
	if int(bs.count(errstr)) > 2:
		print('NO')
	else:
		print('YES')
t = int(input())
for _ in range(t):
	(n, c) = map(int, input().split())
	bs = input()
	solve(c, n, bs * 2)
