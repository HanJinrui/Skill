(s, k) = (input(), 0)
for i in range(1, len(s)):
	if int(s[i - 1] + s[i]) % 4 == 0:
		k += i
print(k + sum((s.count(d) for d in '048')))
