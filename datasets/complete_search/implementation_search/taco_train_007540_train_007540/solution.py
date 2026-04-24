n = input()[0]
(h, m) = map(int, input().split(':'))
if 23 < h or ('2' > n and (not 0 < h < 13)):
	h = 1 + (9 + h) % 10
if 59 < m:
	m -= 40
print('{:02}:{:02}'.format(h, m))
