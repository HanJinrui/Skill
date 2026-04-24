n = int(input())
a = map(int, input().split(' '))
m = 10 ** 9 + 7
p = pow(2, n, m) - 1
y = n - 2
s = 0
i = 0
for v in a:
	s += v * p
	s %= m
	if y >= i:
		p += pow(2, y - i, 2 * m) - pow(2, i, 2 * m)
		p %= m
		i += 1
print(s)
