n = int(input())
a = [0] * 1010
b = [0] * 2010
S = 1000000007
W = 0
b = list(map(int, input().strip().split()))[:n]
for i in range(0, n):
	a.insert(i, b[i])
while not a[n - 1]:
	n -= 1
for w in range(0, n + 1):
	for i in range(0, n):
		b[i] = a[i]
	for i in range(w, n):
		if b[i]:
			b[i] -= 1
	w0 = 0
	w1 = 0
	la = 0
	for i in range(0, n):
		w0 += max(0, b[i] - la)
		w1 += b[i]
		la = b[i]
	T = 2 * n + 2 + (n - w) + 3 * w1 + 2 * w0
	for i in range(0, n):
		if T < S:
			S = T
			W = w
for i in range(W, n):
	if a[i]:
		a[i] -= 1
for i in range(0, n):
	while a[i]:
		j = i
		while a[j]:
			a[j] -= 1
			j += 1
		l = j - i
		for k in range(0, l):
			print('AR', end='')
		print('A', end='')
		for k in range(0, l):
			print('L', end='')
		print('A', end='')
	print('AR', end='')
print('A', end='')
for i in range(W, n):
	print('L', end='')
print('A', end='')
