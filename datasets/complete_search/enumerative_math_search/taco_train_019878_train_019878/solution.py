(n, b) = map(int, input().split())
r = 1 << 60
i = 2
while i * i <= b:
	m = n
	s = c = 0
	while b % i == 0:
		c += 1
		b //= i
	if c:
		while m:
			m //= i
			s += m
		r = min(r, s // c)
	i += 1
s = 0
if b > 1:
	while n:
		n //= b
		s += n
	r = min(r, s)
print(r)
