from sys import stdin
input = stdin.buffer.readline
ans = ''

def f(a, b, c):
	global ans
	if a & 1 & (b & 1) and (not a == b == 1):
		ans += f'+{c}\n'
		a += 1
		b += 1
	while (a & 1 ^ 1) & (b & 1 ^ 1):
		ans += f'/{c}\n'
		a >>= 1
		b >>= 1
	return (a, b)
(a, b, c, d) = map(int, input().split())
while a + b + c + d > 4:
	(p, q, r, s) = (a, b, c, d)
	(a, b) = f(a, b, 1)
	(b, c) = f(b, c, 2)
	(c, d) = f(c, d, 3)
	(d, a) = f(d, a, 4)
	if a == p and b == q and (c == r) and (d == s):
		if a & 1 ^ 1:
			ans += '+1\n'
			a += 1
			b += 1
		elif b & 1 ^ 1:
			ans += '+2\n'
			b += 1
			c += 1
		elif c & 1 ^ 1:
			ans += '+3\n'
			c += 1
			d += 1
		else:
			ans += '+4\n'
			d += 1
			a += 1
print(ans)
