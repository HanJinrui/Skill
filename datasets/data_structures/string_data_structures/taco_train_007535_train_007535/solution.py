a = {}
for _ in range(int(input())):
	b = input()
	print(b + str(a[b]) if a.setdefault(b, 0) else 'OK')
	a[b] += 1
