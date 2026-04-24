for _ in range(int(input())):
	(a, b, c) = map(int, input().split())
	carry = 0
	for i in range(30):
		(x, y, z) = (a >> i & 1, b >> i & 1, c >> i & 1)
		carry ^= x == y and y != z
	print('YES' if not carry else 'NO')
