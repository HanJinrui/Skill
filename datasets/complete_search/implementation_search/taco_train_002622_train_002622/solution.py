(h, m) = map(int, input().split(':'))
m += h * 60
r = 0
while f'{m // 60:02}' != f'{m % 60:02}'[::-1]:
	m = (m + 1) % 1440
	r += 1
print(r)
