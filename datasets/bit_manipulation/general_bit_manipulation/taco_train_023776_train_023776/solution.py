(n, m) = map(int, input().split())
a = [int(x) for x in input().split()]
m -= 1
b = 1
while b < m:
	b <<= 1
while b:
	if b & m:
		a = [a[i] ^ a[(i + b) % n] for i in range(n)]
	b >>= 1
print(*a)
