def fwht(a):
	h = 1
	while h < len(a):
		for i in range(0, len(a), h << 1):
			for j in range(i, i + h):
				k = j + h
				x = a[j]
				y = a[k]
				a[j] = x + y
				a[k] = x - y
		h <<= 1
n = int(input())
bits = 16
a = [0] * (1 << bits)
a[0] = 1
xor = 0
for i in range(n):
	xor ^= int(input())
	a[xor] += 1
fwht(a)
for i in range(len(a)):
	a[i] *= a[i]
fwht(a)
bits += 1
best = 1
high = a[1] >> bits
for i in range(2, len(a)):
	x = a[i] >> bits
	if x > high:
		high = x
		best = i
print(best, high)
