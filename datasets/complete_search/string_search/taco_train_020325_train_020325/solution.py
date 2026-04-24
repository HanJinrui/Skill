(a, b) = (input(), input())
(n, m) = (len(a), len(b))
s = ''
k = c = 0
if m > n:
	(a, b, n, m) = (b, a, m, n)
for ch in a:
	k += 1
	s += ch
	if n // k * s == a and m // k * s == b:
		c += 1
print(c)
