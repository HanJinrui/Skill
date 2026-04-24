def so(s):
	mod = 10 ** 9 + 7
	C1 = [0] * 26
	C2 = [0] * 676
	C3 = [0] * 676
	count = 0
	r26 = list(range(26))
	for c in s:
		k = ord(c) - 97
		p = 26 * k - 1
		q = k - 26
		for i in r26:
			q += 26
			p += 1
			count += C3[q]
			C3[p] += C2[p]
			C2[p] += C1[i]
		C1[k] += 1
	return count % mod
a = input()
print(so(a))
