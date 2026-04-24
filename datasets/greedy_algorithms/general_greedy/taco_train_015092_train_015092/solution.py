n = input()
digits = [0 for x in range(10)]
for x in n:
	digits[int(x)] += 1
best = -1
b1 = ''
b2 = ''
types = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
best = -1
b1 = ''
b2 = ''
for (a, b) in types:
	if digits[a] and digits[b]:
		d1 = digits[:]
		d2 = digits[:]
		d1[a] -= 1
		d2[b] -= 1
		s1 = str(a)
		s2 = str(b)
		for (i, x) in enumerate(d1):
			num = min(x, d2[9 - i])
			s1 += str(i) * num
			s2 += str(9 - i) * num
			d1[i] -= num
			d2[9 - i] -= num
		num = min(d1[0], d2[0])
		s1 = '0' * num + s1
		s2 = '0' * num + s2
		d1[0] -= num
		d2[0] -= num
		if len(s1) > best:
			best = len(s1)
			for (i, x) in enumerate(d1):
				s1 += str(i) * x
			for (i, x) in enumerate(d2):
				s2 += str(i) * x
			b1 = s1
			b2 = s2
if best == -1:
	for x in range(10):
		b1 += str(x) * digits[x]
		b2 += str(x) * digits[x]
print(b1[::-1])
print(b2[::-1])
