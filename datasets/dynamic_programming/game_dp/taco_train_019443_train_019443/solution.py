(w, b) = map(int, input().split())
(k, p, q, s) = (0, 0, 1, w + b)
while q != 0 and k < s:
	d = q * w / s
	p += d
	q -= d
	s -= 1
	d = q * w / s
	q -= d
	s -= 1
	k += 1
print(p)
