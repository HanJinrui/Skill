a = 0
b = 0
maxi = 0
for i in range(int(input())):
	(p1, p2) = map(int, input().split())
	a = a + p1
	b = b + p2
	if abs(a - b) > maxi:
		maxi = abs(a - b)
		if a > b:
			d = 1
		else:
			d = 2
print(d, maxi)
