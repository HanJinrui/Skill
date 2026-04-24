(a, b, c) = [int(x) for x in input().split()]
l = []
for i in range(1, 82):
	x = b * i ** a + c
	if (x > 0 and x < 10 ** 9) and sum(map(int, str(x))) == i:
		l.append(x)
print(len(l))
print(*l)
