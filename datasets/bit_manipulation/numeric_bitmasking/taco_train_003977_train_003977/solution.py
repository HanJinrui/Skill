for _ in range(int(input())):
	(a, b, c) = map(int, input().split())
	ans = 0
	v = 1
	for i in range(33):
		if a == b and b == c:
			ans = 1
			break
		elif a & v == b & v and b & v == c & v:
			break
		elif a & v == b & v:
			c += v
		elif a & v == c & v:
			b += v
		else:
			a += v
		v *= 2
	if ans:
		print('YES')
	else:
		print('NO')
