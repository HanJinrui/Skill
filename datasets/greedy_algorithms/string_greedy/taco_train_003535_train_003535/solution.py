I = input
for _ in [0] * int(I()):
	(n, k) = map(int, I().split())
	r = ''
	a = [0] * 201
	for x in I():
		a[ord(x) - 97] += 1
	i = a[n // k] = 0
	while i < k:
		j = a.index(i)
		r += chr(97 + j)
		i += 1
		a[j] = i
	print(r)
