for i in range(int(input())):
	(a, b, c, d) = map(int, input().split())
	print(max(b * 7, c * a + d * (7 - a)))
