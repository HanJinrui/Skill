for i in range(int(input())):
	(d, c) = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	e = 0
	if sum(a) >= 150:
		e += d
	if sum(b) >= 150:
		e += d
	print('YES' if e > c else 'NO')
