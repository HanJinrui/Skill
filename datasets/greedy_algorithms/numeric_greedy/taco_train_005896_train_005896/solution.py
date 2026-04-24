(x, a) = map(int, input().split())
b = c = a
res = 0
while a < x:
	(a, b, c) = (b, c, b + c - 1)
	res += 1
print(res)
