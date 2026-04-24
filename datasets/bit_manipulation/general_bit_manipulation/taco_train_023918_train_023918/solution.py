def popcount(N):
	n = abs(N)
	p = 0
	b = 0
	while n > 1 << b:
		b += 1
	while b > 0:
		m = 1 << b
		if n & m:
			n ^= m
			p += b * (m >> 1) + n
		b -= 1
	if N < 0:
		return 32 * N + p
	else:
		return p
T = int(input())
for t in range(T):
	(A, B) = map(int, input().split())
	print(popcount(B + 1) - popcount(A))
