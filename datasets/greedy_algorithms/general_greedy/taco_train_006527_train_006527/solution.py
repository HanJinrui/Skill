s = input()
t = input()
(e, r) = (len(s), len(t))
(q, w) = (0, 0)
while q < e and w < r:
	if s[q] == t[w]:
		q += 1
	w += 1
t = t[::-1]
s = s[::-1]
(n, m) = (0, 0)
while n < e and m < r:
	if s[n] == t[m]:
		n += 1
	m += 1
m = r - m + 1
print([0, m - w][m > w])
